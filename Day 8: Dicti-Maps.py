//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        HashMap<String, Integer> phonebookDict = new HashMap<String,Integer>();
        for(int i = 0; i < n; i++)
        {
            String name = in.next();
            int phone = in.nextInt();
            // Write code here
            phonebookDict.put(name,phone);
        }
        while(in.hasNext()){
            String s = in.next();
            // Write code here
            boolean isKeyPresent = phonebookDict.containsKey(s);
            if(isKeyPresent== true)
            {
                System.out.println(s+"="+(phonebookDict.get(s)));
            }
            else
            System.out.println("Not found");
        }
        in.close();
    }
}
