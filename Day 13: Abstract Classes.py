

// Declare your class here. Do not use the 'public' access modifier.
    // Declare the price instance variable
    class MyBook extends Book{
     int prise1;   
    
    /**   
    *   Class Constructor
    *   
    *   @param title The book's title.
    *   @param author The book's author.
    *   @param price The book's price.
    */
    // Write your constructor here
    MyBook(String t,String a,int p)
    {
        super(t,a);
        prise1=p;
    }
    
    /**   
    *   Method Name: display
    *   
    *   Print the title, author, and price in the specified format.
    **/
    // Write your method here
    void display()
    {
        System.out.println("Title: "+title);
        System.out.println("Author: "+author);
        System.out.println("Price: "+ prise1);
    }
    
// End class
    }
