package Java;
import java.net.*;
import java.io.*;

public class test {
    public static void main(String[] args) throws Exception {
        URL yahoo = new URL("https://example.com/");
        URLConnection yc = yahoo.openConnection();
        BufferedReader in = new BufferedReader(new InputStreamReader(yc.getInputStream()));
        String inputLine;
        while ((inputLine = in.readLine()) != null) 
            System.out.println(inputLine);
        in.close();
    }
}

