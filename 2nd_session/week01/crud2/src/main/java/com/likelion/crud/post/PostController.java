package com.likelion.crud.post;
//import org.slf4j.Logger;
//import org.slf4j.LoggerFactory;
//import org.springframework.stereotype.Controller;
//import org.springframework.web.bind.annotation.*;
//
//import java.util.ArrayList;
//import java.util.List;
//
//@Controller
//@ResponseBody
//@RequestMapping("post")
//public class PostController {
////    private static final Logger logger=LoggerFactory.getLogger(PostController.class);
//    private static final Logger logger= LoggerFactory.getLogger(PostController.class);
//    private final List<PostDto> postList;
//
//    public PostController(){
//        postList=new ArrayList<>();
//    }
//    @PostMapping("create")
//    public void createPost(@RequestBody PostDto postDto){
//        logger.info(postDto.toString());
//        this.postList.add(postDto);
//    }
//
//    @GetMapping("read-all")
//    public List<PostDto> readPostAll(){
//        logger.info("in read all");
//        return this.postList;
//    }
//
//    @GetMapping("read-one")
//    public PostDto readPostOne(@RequestParam("id") int id){
//        logger.info("in read one");
//        return this.postList.get(id);
//    }
//
//    @PostMapping("update")
//    public void updatePost(
//            @RequestParam("id") int id,
//            @RequestBody PostDto postDto
//    ){
//        PostDto targetPost=this.postList.get(id);
//        if(postDto.getTitle()!=null){
//            targetPost.setTitle(postDto.getTitle());
//        }
//        if(postDto.getContent()!=null){
//            targetPost.setContent(postDto.getContent());
//        }
//        if(postDto.getWriter()!=null){
//            targetPost.setWriter(postDto.getWriter());
//        }
//        this.postList.set(id,targetPost);
//    }
//
//    @DeleteMapping("delete")
//    public void deletePost(@RequestParam("id") int id){
//        this.postList.remove(id);
//    }
//}

import com.google.gson.Gson;
import com.likelion.crud.aspect.LogExecutionTime;
import com.likelion.crud.aspect.LogArguments;
import com.likelion.crud.aspect.LogReturn;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;


@RestController
@RequestMapping("Post")
public class PostController{
    private static final Logger logger= LoggerFactory.getLogger(PostController.class);
    private final PostService postService;
    //private final Gson gson;
    public PostController(@Autowired PostService postService, @Autowired Gson gson){
        this.postService=postService;
        //this.gson=gson.getGson();
        logger.info(gson.toString());
    }

    @LogArguments
    @PostMapping()
    @ResponseStatus(HttpStatus.CREATED)
    public void createPost(@Valid @RequestBody PostDto postDto){
        this.postService.createPost(postDto);
    }

    @LogReturn
    @GetMapping("{id}")
    public PostDto readPost(@PathVariable("id") int id){
        return this.postService.readPost(id);
    }

    @LogExecutionTime
    @GetMapping("")
    public List<PostDto> readPostAll(){
        return this.postService.readPostAll();
    }

    @PutMapping("{id}")
    @ResponseStatus(HttpStatus.ACCEPTED)
    public void updatePost(@PathVariable("id") int id, @RequestBody PostDto postDto){
        this.postService.updatePost(id, postDto);
    }
    @DeleteMapping("{id}")
    @ResponseStatus(HttpStatus.ACCEPTED)
    public void deletePost(@PathVariable("id") int id){
        this.postService.deletePost(id);
    }
    @GetMapping("test-log")
    public void testLog() {
        logger.trace("TRACE");
        logger.debug("DEBUG");
        logger.info("inFo");
        logger.warn("WARN");
        logger.error("ERRORR");
    }

    @PostMapping("test-valid")
    public void testValue(@Valid @RequestBody ValidTestDto dto){
        logger.info(dto.toString());
    }
}

