package com.likelion.crud.post;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

@Component
@Profile("local")
public class ProfileComponent {
    private static final Logger logger=LoggerFactory.getLogger(ProfileComponent.class);
    public ProfileComponent(){
        logger.info("profile component profile: local");
    }
}
