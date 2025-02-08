// Jared Lewis, Financial Calculater C
#include <stdio.h>
#include <math.h>


int main(void){
    // print statement that welcomes my user, and tells them what the program does.
    printf("\n");
    printf("Hi there! wlecome to my program!\n");
    printf("This program will calculate the best way to spend your money.\n");
    printf("\n\n");
    // ask what their income is (variable an input)
    int income;
    printf("What is your monthly income?:");
    scanf("%d", &income);

    // ask what their rent is (variable an input)
    int rent;
    printf("How much does your monthly rent cost?:");
    scanf("%d", &rent);

    // ask what their utilities is (variable an input)
    int utilities;
    printf("How much does your monthly utilities cost?:");
    scanf("%d", &utilities);

    // ask what their groceries is (variable an input)
    int groceries;
    printf("How much does your monthly groceries cost?:");
    scanf("%d", &groceries);

    // ask what their transportation is (variable an input)
    int transportation;
    printf("How much does your monthly transportation cost?:");
    scanf("%d", &transportation);

    // calculate savings as 10% of income (income*.1) (variable)
    float savings = income * 0.1;

    // calculate spending as income-savings-rent-utilities-groceries-trensportation (variable)
    float spending = (float)income - savings - rent - utilities - groceries - transportation;

    // calculate percent income of rent (rent/income *100) (variable)
    float per_rent = (float)rent / income * 100;

    // calculate percent income of utilities (utilities/income *100) (variable)
    float per_utilities = (float)utilities / income * 100;

    // calculate percent income of groceries (groceries/income *100) (variable)
    float per_groceries = (float)groceries / income * 100;

    // calculate percent income of transportation (transportation/income *100) (variable)
    float per_transportation = (float)transportation / income * 100;

    // calculate percent income of spending (spending/income *100) (variable)
    float per_spending = (float)spending / income * 100;

    // your rent is $XX.XX and which is XX% of your income. (print)
    printf("Your rent is $%d which is %.2f%% of your income.\n", rent, per_rent);

    // your utilities is $XX.XX and which is XX% of your income. (print)
    printf("Your utilities is $%d which is %.2f%% of your income.\n", utilities, per_utilities);

    // your groceries is $XX.XX and which is XX% of your income. (print)
    printf("Your groceries is $%d which is %.2f%% of your income.\n", groceries, per_groceries);

    // your transportation is $XX.XX and which is XX% of your income. (print)
    printf("Your transportation is $%d which is %.2f%% of your income.\n", transportation, per_transportation);

    // your savings is $XX.XX and which is XX% of your income. (print)
    printf("Your savings is $%.2f which is 10%% of your income.\n", savings);

    // your spending is $XX.XX and which is XX% of your income. (print)
    printf("Your spending is $%.2f which is %.2f%% of your income.\n", spending, per_spending);
    return 0;
}