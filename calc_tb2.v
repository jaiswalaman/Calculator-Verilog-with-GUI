`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   09:17:36 10/08/2018
// Design Name:   Calculator
// Module Name:   /home/ise/Downloads/CP-1_Calculator/CP-1_Calculator/calc_tb2.v
// Project Name:  CP-1_Calculator
// Target Device:  
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
////////////////////////////////////////////////////////////////////////////////

module calc_tb2;

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
reg [13:0] mem[1:0]; 
integer id ;
integer i; 
   
	initial begin
		// Initialize Inputs
id=$fopen("//home//ise//Documents//out1.txt","w"	);
    for(i=0;i<2;i=i+1)
	 begin
	 $readmemb("//home//ise//Documents//in.txt",mem);		
                  string[13:0]=mem[i];
	 #10;
       $fwrite(id,"%b\n",res);		
		
        #100;
		// Add stimulus here
      end
				$fclose(id);
		end
      
endmodule

