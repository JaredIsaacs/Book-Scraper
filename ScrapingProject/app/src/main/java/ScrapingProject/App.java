package ScrapingProject;

import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;
import org.jsoup.nodes.Element;

public class App {
    public static String bookChapter;
    
    
    public String getTranslator(Elements bookContent){
        String translator = "";
        translator = bookContent.select("p:contains(Translator)").text();
        
        if(translator.split(" ").length > 4){
            bookChapter = bookChapter.replace(translator, "");
            String[] temp = translator.split(" ");
            translator = temp[0] + " " + temp[2];
        }
        else if(translator.split(" ").length > 2){
            bookChapter = bookChapter.replace(translator, "");
            String[] temp = translator.split(" ");
            translator = temp[0] + " " + temp[1];
        }
        
        bookChapter = bookChapter.replace(translator, "");
        return translator;
    }
    
    
    public String getProofreader(Elements bookContent){
        String proofreader = "";
        proofreader = bookContent.select("p:contains(Proofreader)").text();

        if(proofreader.split(" ").length > 2){            
            bookChapter = bookChapter.replace(proofreader, "");
            String[] temp = proofreader.split(" ");
            proofreader = temp[0] + " " + temp[1];
        }
        
        bookChapter = bookChapter.replace(proofreader, "");
        return proofreader;
    }
    
    
    public void scrapeSite(String site) throws IOException{
        Document doc;
        Elements bookContent;
        
        String bookChapterNum;

        String bookTitle;
        
        
        doc = Jsoup.connect(site).get();
        
        Element test = doc.getElementById("wp-manga-current-chap");
        bookContent = doc.getElementsByClass("reading-content");
        bookChapterNum = bookContent.first().getElementById("wp-manga-current-chap").attr("value"); //Find the attribute value. Which is typically the chapter number.
        bookTitle = bookContent.select("b").first().text(); //select grabs the first <h3> found. 
        bookChapter = bookContent.text().replaceAll(bookTitle, "");
        
        
        
        System.out.println("Chapter: " + bookChapterNum);
        System.out.println("Title: " + bookTitle);
        System.out.println(getTranslator(bookContent) + " " + getProofreader(bookContent));
        System.out.println(bookChapter);
        
        
    }

    
    public static void main(String[] args) {
        try{
            new App().scrapeSite("https://reaperscans.com/series/im-not-a-regressor/chapter-2/");
        }catch(IOException e){
            System.out.println("error: " + e.getMessage());
        }
        
    }
}
