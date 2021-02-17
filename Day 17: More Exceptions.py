
import java.lang.*;
//Write your code here
class Calculator{
    int power(int a,int b) throws Exception
    {
        Exception t = new Exception("n and p should be non-negative");
        int r=1;
        if (a>=0 && b>=0)
        {
            for(int i=1;i<=b;i++)
            r=r*a;
            return r;
        }
        else
        throw t;
    }
}
