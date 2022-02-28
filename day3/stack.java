class StackMemoryFullException extends Exception
{
	public String toString()
	{
		return("Your Stack Memory is Full, Please Remove some items to push further");
	}	
}
class StackEmptyException extends Exception
{
	public String toString()
	{
		return("The Stack you are trying to access is Empty");
	}	
}
class Stack<T>
{
	int MAX=100;
	ArrayList<T> list = new ArrayList<T>();
	Stack(int max)
	{	
		MAX=max;
	}
	void push(T obj) throws StackMemoryFullException
	{
		if(list.size()==MAX)
			throw new StackMemoryFullException();
		list.add(obj);
	}
	T pop() throws StackEmptyException
	{
		if(list.size()==0)
			throw new StackEmptyException();
		T temp=list.get(0);
		list.remove(list.size()-1);
		return(temp);
	}
	T peek() throws StackEmptyException
	{
		if(list.size()==0)
			throw new StackEmptyException();
		T temp=list.get(list.size()-1);
		return(temp);
	}
	public String toString()
	{
		return(list.toString());
	}
}
class Main
{
	public static void main(String[] args)
	{
		try
		{
			Stack<Integer> t=new Stack<Integer>();
			t.push(1);
			t.push(2);
			t.push(3);
			System.out.println(t);
			t.pop();
			System.out.println(t);
			t.push(4);
			t.push(5);
			System.out.println(t);
		}
		catch(StackEmptyException e)
		{
			e.printStackTrace();
		}
		catch(StackMemoryFullException e)
		{
			e.printStackTrace();
		}
	}
}