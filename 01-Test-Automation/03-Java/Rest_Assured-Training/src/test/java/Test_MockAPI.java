import io.restassured.http.*;
import org.json.simple.*;
import org.testng.annotations.*;

import static io.restassured.RestAssured.*;
public class Test_MockAPI {

    @BeforeTest
    public void setUp()
    {
        /*--Initialize broowsers--*/

    }

    @Test(priority = 0)
    public void test_get(){
         baseURI = "http://localhost:3000/";

         given()
                 // params is query params i.e. http://localhost:3000/subjects/?name=Automation
                 .params("name", "Automation")
                 .get("/subjects")
                 .then()
                 .statusCode(200)
                 .log().all();
}

    @Test(priority = 0)
    public void test_post(){
        JSONObject request = new JSONObject();
        request.put("firstName", "Mickey");
        request.put("lastName", "Mouse");
        request.put("subjectId", "1");

        baseURI = "http://localhost:3000/";
        given()
                .contentType(ContentType.JSON)
                .accept(ContentType.JSON)
                .header("Content-Type", "Application/json")
                .body(request.toJSONString())
                .when()
                .post("/users")
                .then()
                .statusCode(201)
                .log().all();
        }

    @Test(priority = 0)
    public void test_post2(){
        JSONObject request = new JSONObject();
        request.put("firstName", "Tom");
        request.put("lastName", "Cat");
        request.put("subjectId", "1");

        baseURI = "http://localhost:3000/";
        given()
                .contentType(ContentType.JSON)
                .accept(ContentType.JSON)
                .header("Content-Type", "Application/json")
                .body(request.toJSONString())
                .when()
                .post("/users")
                .then()
                .statusCode(201)
                .log().all();
    }

    @Test(priority = 1)
    public void patch(){
        JSONObject request = new JSONObject();
        request.put("firstName", "Minnie");
        baseURI = "http://localhost:3000/";
        given()
                .contentType(ContentType.JSON)
                .accept(ContentType.JSON)
                .header("Content-Type", "Application/json")
                .body(request.toJSONString())
                .when()
                .patch("/users/4")
                .then()
                .statusCode(200)
                .log().all();
    }
    @Test(priority = 1)
    public void put(){
        JSONObject request = new JSONObject();
        request.put("firstName", "Donald");
        request.put("lastName", "Duck");
        request.put("subjectId", "1");
        baseURI = "http://localhost:3000/";
        given()
                .contentType(ContentType.JSON)
                .accept(ContentType.JSON)
                .header("Content-Type", "Application/json")
                .body(request.toJSONString())
                .when()
                .patch("/users/5")
                .then()
                .statusCode(200)
                .log().all();
    }

    @Test(priority = 2)
    public void test_delete1 (){
        baseURI = "http://localhost:3000/";
        when()
                .delete("/users/4")
                .then().statusCode(200);
    }

    @Test(priority = 2)
    public void test_delete2 (){
        baseURI = "http://localhost:3000/";
        when()
                .delete("/users/5")
                .then().statusCode(200);
    }


 /*   @AfterTest
    public void tearDown()
    {
        // quick and dirty cleanup as leaves 2 items (Ids 4 & 5)
        for (int i = 4; i<8; i++){
            baseURI = "http://localhost:3000/users/";
            String fullURI = baseURI + i + "/";
            when()
                    .delete(fullURI)
                    .then().statusCode(200);
        }
    }*/
}
