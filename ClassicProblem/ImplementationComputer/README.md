# Implementation Computer(String)

## Topic

stack

[Reverse Polish notation wiki](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

## Problem description

Enter a text calculation formula and calculate the result

* input limit :
1. String Type
2. Operators and numbers are separated by blanks
3. Valid range of numbers : -10000 ~ 10000

## The essential

Inorder expression converted to reverse Polish expression

中序表達式轉換為逆波蘭表達式

```java
import java.util.Stack;

public class InfixToPostfix {
    
    // 定義運算子的優先級
    private static int getPrecedence(char ch) {
        switch (ch) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            case '^':
                return 3;
        }
        return -1;
    }
    
    // 將中序表達式轉換為逆波蘭表達式
    public static String infixToPostfix(String infix) {
        StringBuilder postfix = new StringBuilder();
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < infix.length(); i++) {
            char ch = infix.charAt(i);
            // 如果是運算數，直接輸出到輸出字串
            if (Character.isLetterOrDigit(ch)) {
                postfix.append(ch);
            }
            // 如果是左括號，壓入堆疊
            else if (ch == '(') {
                stack.push(ch);
            }
            // 如果是右括號，將堆疊中的運算子依序彈出到輸出字串，直到左括號為止
            else if (ch == ')') {
                while (!stack.isEmpty() && stack.peek() != '(') {
                    postfix.append(stack.pop());
                }
                if (!stack.isEmpty() && stack.peek() != '(') {
                    return "Invalid Expression";
                } else {
                    stack.pop();
                }
            }
            // 如果是運算子，將堆疊中優先級較高的運算子依序彈出到輸出字串
            else {
                while (!stack.isEmpty() && getPrecedence(ch) <= getPrecedence(stack.peek())) {
                    postfix.append(stack.pop());
                }
                stack.push(ch);
            }
        }
        // 將堆疊中剩餘的運算子依序彈出到輸出字串
        while (!stack.isEmpty()) {
            postfix.append(stack.pop());
        }
        return postfix.toString();
    }
    
    // 測試程式
    public static void main(String[] args) {
        String infix = "a+b*(c^d-e)^(f+g*h)-i";
        String postfix = infixToPostfix(infix);
        System.out.println(postfix);
        // 輸出：abcd^e-fgh*+^*+i-
    }
}
```

## Test Results
```
23 + 58 + 7 - ( 10 + 3 ) - ( 3 - 2 - ( 5 + 4 - ( 8 - 2 ) + 8 ) )
reverseStack: [23, 58, +, 7, +, 10, 3, +, -, 3, 2, -, 5, 4, +, 8, 2, -, -, 8, +, -, -]
Calculation results： 85
-----------------------------------------------------
-2 + 10 + 7 - ( -10 + 3 ) 
reverseStack: [-2, 10, +, 7, +, -10, 3, +, -]
Calculation results： 22
-----------------------------------------------------
3 ^ 2 + 4
reverseStack: [3, 2, ^, 4, +]
Calculation results： 13
-----------------------------------------------------
( 2 * 2 ) ^ 2 + 4
reverseStack: [2, 2, *, 2, ^, 4, +]
Calculation results： 20
-----------------------------------------------------
7 - ( -10 + 12000 )
Exceptions：number out of range.
-----------------------------------------------------
2 * ( 8 / 2 ) - ( -10 + 8 )
reverseStack: [2, 8, 2, /, *, -10, 8, +, -]
Calculation results： 10
-----------------------------------------------------
2 * ( 8 / 3 ) - ( -10 + 8 )
reverseStack: [2, 8, 3, /, *, -10, 8, +, -]
Calculation results： 6
-----------------------------------------------------
 ( 8 / 0 ) - ( -10 + 8 )
reverseStack: [8, 0, /, -10, 8, +, -, ]
Calculation results： Exceptions：/ by zero
-----------------------------------------------------
```

## Reference

[detailed steps](https://blog.hackerpie.com/posts/algorithms/queue-and-stack/reverse-polish-representation/#%E4%BB%8E%E4%B8%AD%E7%BC%80%E8%A1%A8%E8%BE%BE%E5%BC%8F%E8%AF%B4%E8%B5%B7
)

[Java代碼實現前綴、中綴及後綴表達式計算](https://blog.csdn.net/Tian208/article/details/125952301?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-125952301-blog-108881680.235%5Ev32%5Epc_relevant_increate_t0_download_v2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-125952301-blog-108881680.235%5Ev32%5Epc_relevant_increate_t0_download_v2&utm_relevant_index=2)
