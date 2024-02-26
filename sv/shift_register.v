module shift_register
# (
    parameter w = 1
) 
(
    input                clk,
    input                reset,
    input                en,
    input                in,
    output reg [w - 1:0] out_reg
);

    always @ (posedge clk or posedge reset)
        if (reset)
            out_reg <= { w { 1'b0 } };
        else if (en)
            out_reg <= { in, out_reg [w - 1 : 1] };

endmodule