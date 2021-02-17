import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        try
        {
            String S = in.next();
            int inum = Integer.parseInt(S);
            System.out.print(inum);
        }
        catch(Exception e)
        {
            System.out.print("Bad String");
        }
    }
}


/* In python
#!/bin/python3

import sys

S = input().strip()

try: 
    print (int(S))
except ValueError: 
    print ("Bad String")
*/
