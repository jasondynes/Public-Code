import io.restassured.http.*;
import org.json.simple.*;
import org.testng.annotations.*;
import java.util.*;
import static io.restassured.RestAssured.*;

public class Test_Posts {

    @Test
   void post1(){
        Map<String, Object> map = new HashMap<>();
        map.put("name", "Jason Dynes");
        map.put("job", "tester1");
        System.out.println("Raw map looks like this:\n" + map + "\n");

        // convert Map to JSON object using JSON Simple
        JSONObject request = new JSONObject(map);
        System.out.println("Converted JSON Object:\n" + request + "\n");

        // POST command
        given()
                .header("Content-Type", "application/json")
                .contentType(ContentType.JSON)
                .body(request.toJSONString())
                .when()
                .post("https://reqres.in/api/users")
                .then()
                .statusCode(201);
        }

    @Test
    void post2(){
        // code to do without a Map
        JSONObject request = new JSONObject();
        request.put("name", "Test Tester");
        request.put("job", "tester2");
        System.out.println("No MAP - Converted JSON Object:\n" + request);

        // POST command
        given()
                .header("Content-Type", "application/json")
                .contentType(ContentType.JSON)
                .body(request.toJSONString())
                .when()
                .post("https://reqres.in/api/users")
                .then()
                .statusCode(201)
                .log().all();
    }

}

