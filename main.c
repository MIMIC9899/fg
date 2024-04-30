#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CHAR_RANGE 256 // ASCII characters
#define BUFFER_SIZE 60000 // Size of the buffer for writing bits
// +
typedef struct st_Node Node;
struct st_Node {
    unsigned char ch; // Character
    long long freq; // Frequency of the character
    struct Node* left; // Left child
    struct Node* right; // Right child
};
//new - start
typedef struct st_Data Data;
struct st_Data {
    unsigned char buffer[BUFFER_SIZE];
    FILE* file;
    size_t size;
    size_t pos;
    size_t bitpos;
};
//+
void freq_count(size_t* freq, Data* in) {
    do {
        for (size_t i = in->pos; i < in->size; i++)
            freq[in->buffer[i]]++;
        in->pos = 0;
        in->size = fread(in->buffer,1,BUFFER_SIZE,in->file);
    } while (in->size > 0);
}
//+
void free_huffman_tree(Node* node) {
    if (node) {
        free_huffman_tree(node->left);
        free_huffman_tree(node->right);
        free(node);
    }
}

unsigned int writebit(int bit, unsigned int bitpos, unsigned int oct) {
    return oct | (bit << (7 - bitpos));
}

unsigned int clearbit(unsigned int bitpos, unsigned int oct) {
    return oct & ~(1 << (7 - bitpos));
}

void writesym(Data* out, int sym) {
    if (out->bitpos == 0) {
        out->buffer[out->pos] = (unsigned char)sym;
        ++out->pos;
    }
    else {
        out->buffer[out->pos] |= sym >> out->bitpos;
        out->buffer[out->pos + 1] = sym << (8 - out->bitpos);
    }
    ++out->pos;
}

int getbit(Data* in) {
    if (++in->bitpos >= 8) {
        in->bitpos = 0;
        if (++in->pos >= in->size) {
            in->size = fread(in->buffer, 1, BUFFER_SIZE, in->file);
            in->pos = 0;
        }
    }
    int byte = in->buffer[in->pos];
    int bit = (byte >> in->bitpos == 8) & 1;

    return bit;
}
//+
Node* create_node(unsigned char ch, long long freq, Node* left, Node* right) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->ch = ch;
    node->freq = freq;
    node->left = left;
    node->right = right;
    return node;
}
//+
void fill_table(unsigned char* code_table[256], Node* root, unsigned char path[256], size_t length) { 
    if (!root) return;

    if (root->left != NULL) {
        path[length] = '0';
        fill_table(code_table, root->left, path, length + 1);
        path[length] = '1';
        fill_table(code_table, root->right, path, length + 1);
    }
    else {
        path[length] = 0;
        code_table[root->ch] = strcpy((unsigned char*)malloc(length + 1), path, length + 1);
    }
}

void write_tree(Node* root, Data* out) {
    if (!root) return;

    if (root->left != NULL) {
        out->buffer[out->pos] |= 128 >> out->bitpos;
        out->bitpos++;
        if (out->bitpos == 8) {
            out->bitpos = 0;
            out->pos++;
        }
        write_tree(root->left, out);
        write_tree(root->right, out);
    }
    else {
        if (++(out->bitpos) == 8) {
            out->bitpos = 0;
            ++(out->pos);
        }
        printf("%c ", root->ch);
        writesym(out, root->ch);
    }
}

//Node* restore_tree(Data* in) {
//    Node* nd = malloc(sizeof(Node));
//    int bit = getbit(in);
//    if (bit) { // если 1 -- дальше лист, иначе листа нет
//        nd->left = nd->right = NULL;
//        nd->ch = getbyte(in);
//    }
//    else {
//        nd->left = restore_tree(in);
//        nd->right = restore_tree(in);
//    }
//
//    return nd;
//}

void decode(Data* in, Data* out, Node* tree, size_t out_count) {
    size_t i = 0;
    while (i < out_count) {
        Node* cur = tree;
        while (cur->left != NULL) {
            if (getbit(in)) cur = cur->right;
            else cur = cur->left;
        }
        out->buffer[out->pos++] = cur->ch;
        if (out->pos >= BUFFER_SIZE) {
            fwrite(out->buffer, 1, out->pos, out->file);
            out->pos = 0;
        }
        i++;
    }
    fwrite(out->buffer, 1, out->pos, out->file);
}
//+
int cmp(const void* a, const void* b) { // ‘ункци€ дл€  у—орта, естесна не в mktree
    return (*(Node**)b)->freq - (*(Node**)a)->freq;
}
//+
Node* mk_tree(size_t* freq) {
    Node* slice[256];
    size_t n = 0;
    for (int i = 0; i < CHAR_RANGE; i++) {
        if (freq[i] > 0) {
            slice[n++] = create_node((unsigned char)i, freq[i], NULL, NULL);
        }
    }

    while (n > 1) {
        qsort(slice, n, sizeof(Node*), cmp);

        Node* node = (Node*)malloc(sizeof(Node));
        node->left = slice[n - 2];
        node->right = slice[n - 1];
        node->freq = slice[n - 2]->freq + slice[n - 1]->freq;
        //for (int i = 0; i < n; i++) {
        //    printf("%lld ", slice[i]->freq);
        //}
        node->ch = 0;
        slice[n - 2] = node;
        n--;
    }

    return slice[0];
}
//+
unsigned char** create_code_table() {
    unsigned char** codeTable = (unsigned char**)malloc(CHAR_RANGE * sizeof(unsigned char*));
    for (int i = 0; i < CHAR_RANGE; i++) {
        codeTable[i] = NULL;
    }
    return codeTable;
}

int encode(Node* root, Data* out, Data* in) {
    out->bitpos = 0;
    out->pos = 4;
    size_t skip = in->pos;
    size_t input_size = (size_t)ftell(in->file) - skip;
    //fseek(in->size, skip, SEEK_SET);
    out->buffer[0] = (input_size >> 24);
    out->buffer[1] = (input_size >> 16);
    out->buffer[2] = (input_size >> 8);
    out->buffer[3] = (input_size);
    write_tree(root, out);
    
}

int main(void) {
    Data in;
    in.file = fopen("in.txt", "rb");
    char mode;
    if (!fread(&mode, sizeof(char), 1, in.file))
        exit(0);
    
    Data out;
    out.file = fopen("out.txt", "wb");
    
    if (mode == 'c') {
        size_t freq[CHAR_RANGE] = { 0 };

        freq_count(freq, &in);

        for (int i = 0; i < CHAR_RANGE; i++) {
            if (freq[i] > 0) {
                printf("Character '%c' has frequency %lld\n", i, freq[i]);
            }
        }

        unsigned char** code_table = create_code_table();
        Node* root = mk_tree(freq);
        size_t depth = 0;
        unsigned char path[CHAR_RANGE];
        fill_table(code_table, root, path, depth);
        for (int i = 0; i < CHAR_RANGE; i++) {
            if (code_table[i]) {
                printf("Character '%c': %s\n", i, code_table[i]);
            }
        }

        encode(root, &out, &in);

        free_huffman_tree(root);
        for (int i = 0; i < CHAR_RANGE; i++) {
            free(code_table[i]);
        }
        fclose(in.file);
    }

    return 0;
}


//new - end
//
//// +
//Node* create_node(unsigned char ch, long long freq, Node* left, Node* right) {
//    Node* node = (Node*)malloc(sizeof(Node));
//    node->ch = ch;
//    node->freq = freq;
//    node->left = left;
//    node->right = right;
//    return node;
//}
////+
//// comparator function for the priority queue
//int compare(const void* a, const void* b) {
//    Node* node1 = *(Node**)a;
//    Node* node2 = *(Node**)b;
//    return node1->freq - node2->freq;
//}
////+
//void free_huffman_tree(Node* node) {
//    if (node) {
//        free_huffman_tree(node->left);
//        free_huffman_tree(node->right);
//        free(node);
//    }
//}
////+
//Node* build_huffman_tree(long long frequencies[CHAR_RANGE]) {
//    Node* priorityQueue[CHAR_RANGE];
//    int n = 0; // Number of nodes in the priority queue
//
//    // create a leaf node for each character and add it to the priority queue
//    for (int i = 0; i < CHAR_RANGE; i++) {
//        if (frequencies[i] > 0) {
//            priorityQueue[n++] = create_node((unsigned char)i, frequencies[i], NULL, NULL);
//        }
//    }
//
//    // special case: if there's only one unique character, create a dummy internal node
//    if (n == 1) {
//        Node* singleNode = priorityQueue[0];
//        Node* dummyNode = create_node(0, singleNode->freq, NULL, NULL);
//        return create_node(0, singleNode->freq, singleNode, dummyNode);
//    }
//    // Build the Huffman tree by combining the two nodes with the lowest frequency
//    while (n > 1) {
//        // Sort the priority queue
//        qsort(priorityQueue, n, sizeof(Node*), compare);
//
//        // Extract the two nodes with the lowest frequency
//        Node* left = priorityQueue[0];
//        Node* right = priorityQueue[1];
//
//        // Create a new internal node with these two nodes as children
//        Node* node = create_node(0, left->freq + right->freq, left, right);
//
//
//        // test tree
//        /*for (int i = 0; i < n; i++)
//        {
//            printf("%lld ", priorityQueue[i]->freq);
//        }
//        printf("\n");*/
//
//        // Replace the two nodes with the new node in the priority queue
//        priorityQueue[0] = node;
//        priorityQueue[1] = priorityQueue[n - 1];
//        n--;
//    }
//    // The remaining node is the root of the Huffman tree
//    return priorityQueue[0];
//}
////+
//void write_huffman_tree(Node* node, FILE* output) {
//    if (!node) return;
//
//    // If this is a leaf node, write a '1' followed by the character
//    if (!node->left && !node->right) {
//        fputc('1', output);
//        fputc(node->ch, output);
//    }
//    else {
//        // If this is an internal node, write a '0'
//        fputc('0', output);
//        write_huffman_tree(node->left, output);
//        write_huffman_tree(node->right, output);
//    }
//}
//
//Node* read_huffman_tree(FILE* input) {
//    int flag = fgetc(input);
//
//    if (flag == EOF) {
//        return NULL;
//    }
//    if (flag == '1') {
//        // flag is '1' => this is a leaf node
//        unsigned char ch = fgetc(input);
//        //printf("%c ", ch);
//        return create_node(ch, 0, NULL, NULL);
//    }
//    else {
//        // flag is '0' => this is an internal node
//        Node* left = read_huffman_tree(input);
//        Node* right = read_huffman_tree(input);
//        return create_node(0, 0, left, right);
//    }
//}
////+
//void count_frequencies(long long frequencies[CHAR_RANGE]) {
//    FILE* file = fopen("in.txt", "rb"); // Open the file in binary mode
//
//    char mode;
//    if (!fread(&mode, sizeof(char), 1, file))
//        exit(0);
//
//    // Initialize frequencies array
//    for (int i = 0; i < CHAR_RANGE; i++) {
//        frequencies[i] = 0;
//    }
//
//    // Read characters and update their frequencies
//    unsigned char ch;
//    while (!feof(file)) {
//        ch = fgetc(file);
//        frequencies[ch]++;
//    }
//
//    // Close the file
//    fclose(file);
//}
////+
//unsigned char** create_code_table() {
//    unsigned char** codeTable = (unsigned char**)malloc(CHAR_RANGE * sizeof(unsigned char*));
//    for (int i = 0; i < CHAR_RANGE; i++) {
//        codeTable[i] = NULL;
//    }
//    return codeTable;
//}
////+
//void generate_codes(Node* node, unsigned char** codeTable, unsigned char* code, int length) {
//    if (!node) return;
//
//    // has a character?
//    if (!node->left && !node->right) {
//        code[length] = '\0'; // finish code string
//
//        codeTable[node->ch] = (unsigned char*)malloc(length + 1);
//        strcpy((char*)(codeTable[node->ch]), (char*)code);
//    }
//    else {
//        code[length] = '0';
//        generate_codes(node->left, codeTable, code, length + 1);
//
//        code[length] = '1';
//        generate_codes(node->right, codeTable, code, length + 1);
//    }
//}
//
//// write bits to the output file
//void write_bits(FILE* output, unsigned char* code, unsigned char* bitBuffer, int* bitCount, size_t* bitLength) {
//    (*bitLength)++; // increment length of encoded data
//    while (*code) {
//        // Set the bit at the current position in the buffer
//        if (*code == '1') {
//            bitBuffer[*bitCount / 8] |= (1 << (7 - (*bitCount % 8)));
//        }
//        (*bitCount)++;
//
//        code++;
//
//        // If the buffer is full, write it to the file
//        if (*bitCount == BUFFER_SIZE * 8) {
//            fwrite(bitBuffer, 1, BUFFER_SIZE, output);
//            memset(bitBuffer, 0, BUFFER_SIZE); // Clear the buffer
//            *bitCount = 0;
//        }
//    }
//}
//
//void encode_file(const char* inputFilename, const char* outputFilename, unsigned char** codeTable, Node* root) {
//    FILE* input = fopen(inputFilename, "rb");
//    FILE* output = fopen(outputFilename, "wb");
//    if (!input || !output) {
//        perror("Failed to open files");
//        exit(EXIT_FAILURE);
//    }
//
//    char mode;
//    if (!fread(&mode, sizeof(char), 1, input))
//        exit(0);
//    // Keep track of the number of bits written to encode the data
//    size_t bitLength = 0;
//    fwrite(&bitLength, sizeof(bitLength), 1, output); // Write placeholder
//
//    // Then, write the encoded data as before
//    unsigned char bitBuffer[BUFFER_SIZE] = { 0 };
//    int bitCount = 0; // Number of bits in the buffer
//    // First, serialize the Huffman tree and write it to the output file
//    write_huffman_tree(root, output);
//    int ch;
//    while ((ch = fgetc(input)) != EOF) {
//        // Write the bits for the current character to the buffer
//        write_bits(output, codeTable[ch], bitBuffer, &bitCount, &bitLength);
//    }
//
//    // Write any remaining bits in the buffer to the file
//    if (bitCount > 0) {
//        fwrite(bitBuffer, 1, (bitCount + 7) / 8, output); // Write the full bytes of the remaining bits
//    }
//
//    // Before closing the files, seek to the beginning and write the bitLength
//    fseek(output, 0, SEEK_SET); // Skip the space reserved for bitLength
//    fwrite(&bitLength, sizeof(bitLength), 1, output); // Write the actual bitLength
//
//    fclose(input);
//    fclose(output);
//}
//
//void decode_file(const char* inputFilename, const char* outputFilename) {
//    FILE* input = fopen(inputFilename, "rb");
//    FILE* output = fopen(outputFilename, "wb");
//    if (!input || !output) {
//        perror("Failed to open files");
//        exit(EXIT_FAILURE);
//    }
//    char mode;
//    if (!fread(&mode, sizeof(char), 1, input))
//        exit(0);
//    size_t bitLength;
//    if (!fread(&bitLength, sizeof(size_t), 1, input))
//    {
//        exit(0);
//    }
//    // First, deserialize the Huffman tree from the input file
//    Node* root = read_huffman_tree(input);
//
//    // Read the length of the encoded data
//    Node* current = root;
//    unsigned char bitBuffer[BUFFER_SIZE];
//    size_t bytesRead = 0;
//    size_t bitsRead = 0;
//    while (bitsRead < bitLength && ((bytesRead = fread(bitBuffer, 1, BUFFER_SIZE, input)) > 0)) {
//        for (size_t byteIndex = 0; byteIndex < bytesRead; ++byteIndex) {
//            for (int bitIndex = 0; bitIndex < 8; ++bitIndex) {
//                // Determine the current bit
//                int bit = (bitBuffer[byteIndex] >> (7 - bitIndex)) & 1;
//                // Traverse the Huffman tree
//                current = bit ? current->right : current->left;
//
//                // If we reach a leaf node, write the character to the output file
//                if (!current->left && !current->right) {
//                    if (bitsRead < bitLength)
//                    {
//                        bitsRead += 1;
//                        fputc(current->ch, output);
//                    }
//                    current = root; // Go back to the root of the tree for the next character
//                }
//            }
//        }
//    }
//
//    fclose(input);
//    fclose(output);
//}
//
//int main(void) {
//    FILE* input = fopen("in.txt", "rb");
//    char mode;
//    if (!fread(&mode, sizeof(char), 1, input))
//        exit(0);
//
//    if (mode == 'c') {
//        // arr to hold frequencies of characters
//        long long frequencies[CHAR_RANGE] = { 0 };
//
//        count_frequencies(frequencies);
//
//        int isInputEmpty = 1;
//        for (int i = 0; i < CHAR_RANGE; i++) {
//            if (frequencies[i] > 0) {
//                isInputEmpty = 0;
//                break;
//            }
//        }
//
//        if (isInputEmpty) {
//            fclose(input);
//            return 0;
//        }
//
//        // test freq
//        /*for (int i = 0; i < CHAR_RANGE; i++) {
//            if (frequencies[i] > 0) {
//                printf("Character '%c' has frequency %lld\n", i, frequencies[i]);
//            }
//        }*/
//
//        // Build the Huffman tree
//        Node* root = build_huffman_tree(frequencies);
//
//        // Create an empty code table
//        unsigned char** codeTable = create_code_table();
//
//        // Array to hold the current code
//        unsigned char code[CHAR_RANGE];
//        int length = 0; // Current length of the code
//
//        // Generate the Huffman codes
//        generate_codes(root, codeTable, code, length);
//
//        //// test codes
//        //for (int i = 0; i < CHAR_RANGE; i++) {
//        //    if (codeTable[i]) {
//        //        printf("Character '%c': %s\n", i, codeTable[i]);
//        //    }
//        //}
//
//        encode_file("in.txt", "out.txt", codeTable, root);
//
//        free_huffman_tree(root);
//        for (int i = 0; i < CHAR_RANGE; i++) {
//            free(codeTable[i]);
//        }
//        fclose(input);
//    }
//    else if (mode == 'd')
//    {
//        fclose(input);
//        decode_file("in.txt", "out.txt");
//    }
//    else
//        fclose(input);
//
//    return 0;
//}
//
