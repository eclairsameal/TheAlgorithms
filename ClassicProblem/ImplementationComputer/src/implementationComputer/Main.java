package implementationComputer;
// import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

public class Main {
/*  infix notation -> Reverse Polish notation */
	public static Stack<String> infixToReverse (ArrayList<String> formula_array) {
		Stack<String> operatorStack = new Stack();
		Stack<String> reverseStack = new Stack();
		for (String s : formula_array) {
			if (s.matches("-?\\d+")) {
				// 如果是運算數，直接輸出到輸出字串
				// オペランドの場合は直接 reverseStack にプッシュする
				if(Integer.parseInt(s) < -10000 || Integer.parseInt(s) > 10000){
					throw new IllegalArgumentException("number out of range.");
				}
				reverseStack.push(s);
			} else if(s.equals("(")) {
				// 如果是左括號，壓入堆疊
				// 左括弧の場合は、operatorStack にプッシュします
				operatorStack.push(s);
			} else if(s.equals(")")) { 
				// 如果是右括號，將堆疊中的運算子依序彈出到輸出字串，直到左括號為止
				// 右括弧の場合は、operatorStack 内の演算子を reverseStack に順番に左括弧までプッシュします。
				while(!operatorStack.isEmpty() && !operatorStack.peek().equals("(")) {
					reverseStack.push(operatorStack.pop());
				}
				operatorStack.pop();
			} else {  
				// 如果是運算子，將堆疊中優先級較高的運算子依序彈出到輸出字串
				// オペレーターの場合は、operatorStack で優先度の高いオペレーターを順に reverseStack にプッシュします。
				while (!operatorStack.isEmpty() && priority(s) <= priority(operatorStack.peek())) {
					reverseStack.push(operatorStack.pop());
				}
				operatorStack.push(s);
			}
			//print stack details
			//System.out.print(s);
			//printMiddleToBackAllStack(operatorStack, reverseStack);
		}
		// 將堆疊中剩餘的運算子依序彈出到輸出字串
		// operatorStack の残りのオペレーターを backExpressionStack に順番にプッシュします。
		while (!operatorStack.isEmpty()) {
			reverseStack.push(operatorStack.pop());
		}
		System.out.print("reverseStack: ");
		printtStack(reverseStack);
	
		return reverseStack;
	}
	public static int priority(String str) {
		// Set the priority of the operator
		switch(str) {
			case "+":
			case "-":
				return 1;
			case "*":
			case "/":
				return 2;
			case "^":
				return 3;
		}
		return 0;
	}
/* calculate Reverse Polish notation(backExpression() */
	public static int calculateReverse(Stack<String> reverseStack) {
		Stack<Integer> resultStack = new Stack();
		for (String s : reverseStack) {
			if (s.matches("-?\\d+")) {
				resultStack.push(Integer.parseInt(s));
			}else {
				int num1 = resultStack.pop();
				int num2 = resultStack.pop();
				resultStack.push(calculateOperator(num2, num1, s));
			}
			//print stack details
			//System.out.print("resultStack: ");
			//printtStack(resultStack);
		}
		return resultStack.pop();
	}
	public static int calculateOperator(int a, int b, String op){ 
		switch(op) {
			case "+":
				return a + b;
			case "-":
				return a - b;
			case "*":
				return a * b;
			case "/":
				if(b==0) {
					throw new IllegalArgumentException("/ by zero");
				}
				return a / b;
			case "^":
				return (int) Math.pow((double)a, (double)b);
		}
		return 0;
	}

/* print related functions */
	public static void printtStack(Stack<?> stack){  
		// Print the stack of any data type
		String values = Arrays.toString(stack.toArray());
	    System.out.println(values);
	}
	public static void printMiddleToBackAllStack(Stack<?> oStack, Stack<?> bStack){ 
		// Print the stack in MiddleToBack
		System.out.print("operatorStack: ");
		printtStack(oStack);
		System.out.print("reverseStack: ");
		printtStack(bStack);
		System.out.println("-----------------------------------------------------");		
	}
	
	public static void main(String[] args) {
//		Scanner sc = new Scanner(System.in);
//		System.out.println("input: ");
//		String formula = sc.nextLine();
		for (String formula : args) {
			ArrayList<String> formula_array = new ArrayList<String>();
			System.out.println(formula);
			for (String s : formula.split(" ")) {
				formula_array.add(s);
			}
			try {
				Stack<String> reverseStack = infixToReverse (formula_array);
				System.out.print("Calculation results： ");
				System.out.println(calculateReverse(reverseStack));
			}catch(IllegalArgumentException ex){
                System.out.println("Exceptions：" + ex.getMessage());
//                System.out.println("例外原因：");
//                ex.printStackTrace();
			}
			System.out.println("-----------------------------------------------------");
		}
	}
}
