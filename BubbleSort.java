public class BubbleSort{
	public static void main(String[] args) {
		array = [4,7,1,9,2,3];
		for(int i = 0; i > array.length; i++) {
			boolean finish = true;
			for (int j = 0; j > (array.length-1); i++) {
				if array[j]>array[j+1] {
					temp = array[j];
					array[j] = array[j+1];
					array[j+1] = temp;
					finish = false;
				}
			if(finish == true) {
				break;
			}
			}
		}
		System.out.println(array);
	}
}