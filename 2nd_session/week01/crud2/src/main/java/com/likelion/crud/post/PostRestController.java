package com.likelion.crud.post;

import com.likelion.crud.exception.PostNotExistException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("post")
public class PostRestController {
    private static final Logger logger = LoggerFactory.getLogger(PostRestController.class);
    private final List<PostDto> postList;

    public PostRestController() {
        this.postList = new ArrayList<>();
    }

    //http://localhost:8080/post
    //1 createPost
    @PostMapping()
    @ResponseStatus(HttpStatus.CREATED)
    public void createPost(@RequestBody PostDto postDto) {
        logger.info(postDto.toString());
        this.postList.add(postDto);
    }

    //2 get
    //Get /post
    @GetMapping()
    public List<PostDto> readPostAll() {
        logger.info("iin read post all");
        return this.postList;
    }

    //Get/post/0/
    @GetMapping("{id}")
    public PostDto readPost(@PathVariable("id") int id) {
        logger.info("in read post");
        return this.postList.get(id);
    }

    //3 update
    @PutMapping("{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void updatePost(
            @PathVariable("id") int id,
            @RequestBody PostDto postDto
    ){
        PostDto targetPost=this.postList.get(id);
        if (postDto.getTitle()!=null){
            targetPost.setTitle(postDto.getTitle());
        }
        if (postDto.getWriter()!=null){
            targetPost.setWriter(postDto.getWriter());
        }
        if (postDto.getContent()!=null){
            targetPost.setContent(postDto.getContent());
        }
        this.postList.set(id, targetPost);
    }

    //4 delete
    // Delete /post/0
    @DeleteMapping("{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deletePost(
            @PathVariable("id") int id
    ){
        this.postList.remove(id);
    }

    //예외처리 추가
    @GetMapping("/test-exception")
    public void throwException(){
        System.out.println("test-exception");
        throw new PostNotExistException();
    }
}
