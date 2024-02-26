module d_trigger
(
	input CLK,
	input RST,
	input EN,
	input D,
	output Q
);

	reg OUT;
	
	always @(posedge CLK) begin
				if(RST) 
					OUT <= 1'b0; 
				else if (EN)
					OUT <= D;
	end
	
	assign Q = OUT;
endmodule

module testbench;

	logic CLK = 0;
	logic RST = 0;
	logic EN = 1;
	logic D, Q;
	
	d_trigger t(
        .CLK,
        .RST,
        .EN,
        .D,
        .Q
    );
	
	always begin
		#10 CLK = ~CLK;
	end
	
	initial begin
        D = 1;
		EN = 1;
		$display("%b %b %b %b %b", CLK, RST, EN, D, Q);
		RST = 0;
        #10;
		$display("%b %b %b %b %b", CLK, RST, EN, D, Q);
		$finish;
	end


endmodule