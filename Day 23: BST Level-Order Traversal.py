

	static void levelOrder(Node root){
        Queue<Node> queue = new LinkedList<Node>();
      queue.add(root);
      while(queue.peek()!=null)
          {
          Node node =queue.remove();
          System.out.print(""+node.data+" ");
          if(node.left!=null)
              queue.add(node.left);
          if(node.right!=null)
              queue.add(node.right);
      }
      //Write your code here
      
    }

