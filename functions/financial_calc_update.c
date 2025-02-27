// Jared Lewis, Financial Calculator Update C
#include <stdio.h>
#include <math.h>

float income, rent, utilities, groceries, transportation, savings, spending;

void info(char type[],int cost){
    int per = cost/ income *100;
    printf("Your %s is $%d which is %d%% of your income.\n", type, cost, per);
}
float user_input(char type[]){
    float amount;
    printf("How much is your monthly %s?: ", type);
    scanf("%f", &amount);
    return amount;

}
int main(void){
    // print statement that welcomes my user, and tells them what the program does.
    printf("\n");
    printf("Hi there! wlecome to my program!\n");
    printf("This program will calculate the best way to spend your money.\n");

    // collect user inputs
    income = user_input("income");
    rent = user_input("rent");
    utilities = user_input("utilities");
    groceries = user_input("groceries");
    transportation = user_input("transportation");

    // calculate percent of income for each category
    float savings = income * 0.1;
    float spending = (float)income - savings - rent - utilities - groceries - transportation;
    float per_rent = (float)rent / income * 100;
    float per_utilities = (float)utilities / income * 100;
    float per_groceries = (float)groceries / income * 100;
    float per_transportation = (float)transportation / income * 100;
    float per_spending = (float)spending / income * 100;

    // print out the results
    info("rent", rent);
    info("uttilities", utilities);
    info("groceries", groceries);
    info("transportation", transportation);
    info("savings", savings);
    info("spending", spending);
    return 0;
}