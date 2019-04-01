`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Module Name:   /home/ise/CP-1_Calculator/Calc_TestBench.v
// Project Name:  CP-1_Calculator
// Target Device:  
//
//GroupID-16(17114004_17114013)-AbhishekRathod & AnshumanShakya
//GroupID-11(17114008_17114010)-AmanJaiswal & AmitKumar
//
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: Calculator
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
///////////////////////////////////////////////////////////////////////////////

module Calc_TestBench;

	// Inputs
	reg [13:0] string;

	// Outputs
	wire [3:0] res;
	wire [6:0] seven_output;

	// Instantiate the Unit Under Test (UUT)
	Calculator uut (
		.string(string), 
		.res(res), 
		.seven_output(seven_output)
	);
integer i ;
integer j ;

	initial begin
		// Initialize Inputs
		string[13:0]=14'b00000000000000 ;		
		for(i=0;i<16;i=i+1)
		begin
			for(j=0;j<16;j=j+1)
			begin
				string[7:4]= string[7:4]+4'b0001 ;
				string[3:0]=string[11:8]+string[7:4] ;
				string[13:12]=2'b00 ;
				#0.5;
			end; 
				string[11:8] = string[11:8]+4'b0001 ;
		end;
		
		
		 string[13:0]=14'b01000000000000 ;
	 for( i=0;i<16;i=i+1)
	 begin
	  for( j=0;j<16;j=j+1)
	  begin
	  string[7:4]=string[7:4]+4'b0001;
	 string[3:0]=string[11:8]-string[7:4];
      string[13:12] = 2'b01;
	 #0.5;
	  end;
	  string[11:8]=string[11:8]+4'b0001;
	 end;
	 
	 string[13:0]=14'b10000000000000 ;
	 for( i=0;i<16;i=i+1)
	 begin
	  for( j=0;j<16;j=j+1)
	  begin
	  string[7:4]=string[7:4]+4'b0001;
	 string[3:0]=string[11:8]|string[7:4];
	 
      string[13:12] = 2'b10;
	 #0.5;
	  end;
	  string[11:8]=string[11:8]+4'b0001;
	 end;
	 
	  string[13:0]=14'b11000000000000 ;
	 for( i=0;i<16;i=i+1)
	 begin
	  for( j=0;j<16;j=j+1)
	  begin
	  string[7:4]=string[7:4]+4'b0001;
	 string[3:0]=~string[11:8]+4'b0001;
	 
      string[13:12] = 2'b11;
	 #0.5;
	  end;
	  string[11:8]=string[11:8]+4'b0001;
	 end;
	 
	end 
      
endmodule
