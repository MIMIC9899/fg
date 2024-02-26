module counter
# (
    parameter w = 1
) 
(
    input                clk,
    input                reset,
    input                en,
    output reg [w - 1:0] cnt
);

    always @ (posedge clk or posedge reset)
        if (reset)
            cnt <= { w { 1'b0 } };
        else if (en)
            cnt <= cnt + 1'b1;

endmodule

module testbench;

	localparam w = 8;
	logic clk = 0;
	logic reset = 0;
	logic en = 1;
	logic [w - 1:0] cnt;
	
	counter #(w) c1(.clk, .reset, .en, .cnt);
	
	always begin
		#10 clk = ~clk;
	end
	
	initial begin
		reset = 1;
		#20;
		reset = 0;
		$display("%b", cnt);
		#20 $display("%b", cnt);
		#20 $display("%b", cnt);
		#20 $display("%b", cnt);
		
	end
	
endmodule