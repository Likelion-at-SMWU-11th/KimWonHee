package com.likelion.crud.post;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultActions;

import java.util.Arrays;
import java.util.List;

import static org.hamcrest.Matchers.*;
import static org.mockito.BDDMockito.given;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.mock;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

import static org.hamcrest.Matchers.*;

@RunWith(SpringRunner.class)
@WebMvcTest(PostController.class) //mvc 부분 테스트(@Controller)
public class PostControllerTest{
    @Autowired
    private MockMvc mockMvc; //mvc 역할을 가짜로 흉내 (마치 http 클라이언트인 척)

    @MockBean
    private PostService postService;

    @Test
    public void readPost() throws Exception{
        //given 어떤 데이터가 준비되어있다
        //PostEntity가 존재할 때
        final int id=10;
        PostDto testDto=new PostDto(id);
        testDto.setId(id);
        testDto.setTitle("unit title");
        testDto.setContent("unit content");
        testDto.setWriter("unit");


        given(postService.readPost(id)).willReturn(testDto); //postService가 readPost(id)함수를 호출하면 testDto를 리턴한다고 정의

        //when 어떤 행위가 일어났을 때 (함수 호출 등)
        //경로에 GET 요청이 오면
        final ResultActions actions=mockMvc.perform(get("/post/{id}", id))
                .andDo(print());

        //then 어떤 결과가 올것인지
        //PostDto가 반환된다
        actions.andExpectAll(
                status().isOk(),
                content().contentType(MediaType.APPLICATION_JSON),
                jsonPath("$.title", is("unit title")),
                jsonPath("$.content",is("unit content")),
                jsonPath("$.writer", is("unit"))
        );
    }

    @Test
    public void readPostAll() throws Exception{
        //given
        PostDto post1=new PostDto();
        post1.setTitle("title1");
        post1.setContent("test");
        post1.setWriter("test");

        PostDto post2=new PostDto();
        post2.setTitle("title2");
        post2.setContent("test");
        post2.setWriter("test");

        List<PostDto> readAllPost=Arrays.asList(post1, post2);
        given(postService.readPostAll()).willReturn(readAllPost);

        //when
        final ResultActions actions=mockMvc.perform(get("/post"))
                .andDo(print());

        //then
        actions.andExpectAll(
                status().isOk(),
                content().contentTypeCompatibleWith(MediaType.APPLICATION_JSON),
                jsonPath("$", hasSize(readAllPost.size()))
        );
    }

    @Test
    public void updatePost() {
    }
}