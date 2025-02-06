//Jared Lewis, Expressions Practice C
#include <stdio.h>
#include <math.h>


int main(void){
    int expression_one = 7-24/8*4+6;
    printf("%d \n", expression_one);
    //7-24➗8✖️4+6=1

    int expression_two = 18/3-7+2*5;
    printf("%d \n", expression_two);
    //18➗3-7+2✖️5=9

    int expression_three = 6*4/12+72/8-9;
    printf("%d \n", expression_three);
    //6×4➗12+72➗8-9=2

    int expression_four = (17-6/2)+4*3;
    printf("%d \n", expression_four);
    //(17-6➗2)+4✖️3=26

    int expression_five = -2*(1*4-2/2)+6+2-3;
    printf("%d \n", expression_five);
    //-2(1×4-2➗2)+(6+2-3)=-1

    int expression_six = -1*((3-4*7)/5)-2*24/6;
    printf("%d \n", expression_six);
    //-1×[(3-4×7)➗5]-2×24➗6 =-3

    float expression_seven = (3*pow(5,2)/15)-(5-pow(2,2));
    printf("%f \n", expression_seven);
    //(3*5^2/15)-(5-2^2) =4

    float expression_eight = pow(1,4)*pow(2,2)+pow(3,3)-pow(2,5)/4;
    printf("%f \n", expression_eight);
    //(1^4*2^2+3^3)-2^5/4 =23

    float expression_nine = pow(22/2-2*5,2)+pow(4-6/6,2);
    printf("%f \n", expression_nine);
    //(22/2-2*5)^2+(4-6/6)^2 =10
    return(0);
}