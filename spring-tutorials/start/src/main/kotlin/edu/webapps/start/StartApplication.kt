package edu.webapps.start

import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController


//@SpringBootApplication
//@RestController
//class StartApplication {
//  @GetMapping("/hello")
//  fun hello(@RequestParam(value = "name", defaultValue = "World") name: String?): String {
//    return String.format("Hello %s!", name)
//  }
//
//  companion object {
//    @JvmStatic
//    fun main(args: Array<String>) {
//      SpringApplication.run(StartApplication::class.java, *args)
//    }
//  }
//}

//edu.webapps.start.StartApplication

@SpringBootApplication
@RestController
class StartApplication{
  /** Consts/ Statics */
  companion object{
    /**
    @JvmStatic
    fun main(args: Array<String>) {
      //  runApplication<StartApplication>(*args);
      SpringApplication.run(StartApplication::class.java, *args);
    }
    */
  }
  /** Variables */

  /** Constructors */

  /** urls */
  @GetMapping("/hello")
  fun hello(@RequestParam(value = "name", defaultValue = "World") name: String?): String? {
    val output: String = "Hello there! $name";
    return output;
  }

}

/** Static in Kotlin */
// this is another way of writing statics!

fun main(args: Array<String>) {
//  runApplication<StartApplication>(*args);
  SpringApplication.run(StartApplication::class.java, *args);
}

// $ gradle build
// $ gradle tasks
// $ gradle bootRun
