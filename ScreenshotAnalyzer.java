import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;


public class ScreenshotAnalyzer {

    public static void main(
        String[] args
    ) {

        try {

            File file =
                new File("screenshot.png");


            BufferedImage image =
                ImageIO.read(file);


            int width =
                image.getWidth();

            int height =
                image.getHeight();


            System.out.println(
                "Screenshot Analysis"
            );


            System.out.println(
                "Width  : " + width
            );


            System.out.println(
                "Height : " + height
            );


            System.out.println(
                "Type   : Webpage Screenshot"
            );


            System.out.println(
                "Analysis completed successfully."
            );

        }

        catch (Exception e) {

            System.out.println(
                "Error reading screenshot."
            );

        }

    }
}