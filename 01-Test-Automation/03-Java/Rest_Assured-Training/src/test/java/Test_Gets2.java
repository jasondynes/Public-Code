import org.testng.annotations.*;
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

public class Test_Gets2 {

    @Test
    public void test_1(){
        given().
                header("Content-Type", "application/json")
                .get("http://swapi.dev/api/people/1/")
                .then().statusCode(200)
                .body("gender", equalTo("male"))
                .body("films[0]", equalTo("https://swapi.dev/api/films/1/"))
                .body("films", hasItems("https://swapi.dev/api/films/2/", "https://swapi.dev/api/films/1/"))
                .log().all();
    }
}
