import java.util.*;
import java.io.*;

public class Main
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        String str;
        int[][] count = new int[100][4];
        int line = 0;

        while((str = br.readLine()) != null){
            line++;
            for(int i = 0; i < str.length(); i++)
            {
                char cur = str.charAt(i);
                
                if(Character.isLowerCase(cur)) {
                    count[line - 1][0]++;
                } else if (Character.isUpperCase(cur)) {
                    count[line - 1][1]++;
                } else if (Character.isDigit(cur)) {
                    count[line - 1][2]++;
                } else {
                    count[line - 1][3]++;
                }
            }
        }
        
        for(int i = 0; i < line; i++) {
            sb.append(count[i][0] + " " + count[i][1] + " " + count[i][2] + " " + count[i][3] + "\n");
        }
        
        sb.setLength(sb.length() - 1);
        
        System.out.println(sb.toString());
    }
}