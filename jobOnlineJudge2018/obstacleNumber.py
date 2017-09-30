# -*- coding:utf-8 -*-
'''
2.小新是一名小学生，最近妈妈给他送了一款小霸王游戏机，他非常的开心，里面有一款游戏他非常的喜爱。
游戏中，一个模型会在一条隧道中向前运动，途中会遇到很多高高低低，上上下下的障碍物，
小新需要用到不同的操作力度和按键方案来使模型跳到要求的高度从而越过障碍，连续跳高是比较难的操作，
小新反反复复玩了很多遍，都没能前进很多。于是他希望从失败中寻找一些规律，
以便下次再玩时会轻松的越过这些障碍。
我们假设一共有n个障碍物，从左到右分别用1到n来标识。
我们用一个整数ai来表示小新需要在第i个障碍物处恰好跳到ai的高度才可以越过该障碍，如果连续3个障碍物的高度是不递减的，即ai≤ai+1≤ai+2，那么小新会将这里记为障碍难点。注意每个障碍物可以被多次记录，例如连续5个障碍物的高度分别为1 2 3 4
'''
import sys

'''
import java.util.Scanner;
public class t361 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in );

		int n = Integer.parseInt(sc.nextLine());

		String [] a = sc.nextLine().split(" ");
		int []data1 = new int[n];
		for(int i = 0;i<n;i++){
			data1[i]=Integer.parseInt(a[i]);
		}
		int m = Integer.parseInt(sc.nextLine());
		int [] e=new int[m];
		for(int i = 0;i<m;i++){
			String [] b = sc.nextLine().split(" ");
			int r=result(Integer.parseInt(b[0])-1, Integer.parseInt(b[1])-1, data1);
			e[i]=r;
		}
		for(int i=0;i<m;i++){
			System.out.println(e[i]);
		}


	}
	public  static int result(int start,int end,int []data1){
		int [] D=new int[data1.length];
		Arrays.fill(D, 1);
		int index= start;
		for(int i=start+1;i<=end;i++){
			if(data1[index]<=data1[i]){
				D[i]=D[index]+1;
				index=i;
			}else {
				index=i;
			}
		}
		int times=0;
		for(int i=0;i<D.length;i++){
			if(D[i]>=3){
				times++;
			}
		}
		return times;
	}

}
'''