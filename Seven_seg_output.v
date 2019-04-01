`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    10:34:03 10/07/2018 
// Design Name: 
// Module Name:    Seven_seg_output 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
//
//
//GroupID-16(17114004_17114013)-AbhishekRathod & AnshumanShakya
//GroupID-11(17114008_17114010)-AmanJaiswal & AmitKumar
//
//
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module Seven_seg_output(
    input[3:0] bcd_op,
    output reg[6:0] seven_seg_op
    );


always @(bcd_op)
    begin
        case (bcd_op) //case statement
            4'b0000 : seven_seg_op = 7'b0000001;
            4'b0001 : seven_seg_op = 7'b1001111;
            4'b0010 : seven_seg_op = 7'b0010010;
            4'b0011 : seven_seg_op = 7'b0000110;
            4'b0100 : seven_seg_op = 7'b1001100;
            4'b0101 : seven_seg_op = 7'b0100100;
            4'b0110 : seven_seg_op = 7'b0100000;
            4'b0111 : seven_seg_op = 7'b0001111;
            4'b1000 : seven_seg_op = 7'b0000000;
            4'b1001 : seven_seg_op = 7'b0000100;
            //switch off 7 segment character when the bcd digit is not a decimal number.
            default : seven_seg_op = 7'b1111110; 
        endcase
    end

endmodule
