package com.likelion.crud;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

@SpringBootApplication
@EnableJpaAuditing

public class Crud2Application {

    public static void main(String[] args) {
        SpringApplication.run(Crud2Application.class, args);
    }

}
