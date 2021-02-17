import java.util.Scanner;  
  
import java.util.Scanner;  
  
public class PrimeExample3 {  
  
   public static void main(String[] args) 
   {  
       Scanner s = new Scanner(System.in);  
       int n = s.nextInt();  
       for(int i=0;i<n;i++)
       {
        int a = s.nextInt();
        if (isPrime(a))   
           System.out.println("Prime");  
         else 
           System.out.println("Not prime");  
       }
   }  
  
   public static boolean isPrime(int n) 
   {  
       int b=0;
       if (n <= 1)  
           return false;  
       for (int i = 2; i <= Math.sqrt(n); i++) {  
           if (n % i == 0) 
               return false;  
       }
       return true; 
   }  
}  
