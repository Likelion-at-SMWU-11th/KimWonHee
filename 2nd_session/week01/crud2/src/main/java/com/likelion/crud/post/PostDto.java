package com.likelion.crud.post;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

@Getter
@Setter
@NoArgsConstructor
public class PostDto {
    private int id;
    @NotNull //validation annotation(3주차 4-2)
    private String title;
    @Size(max=400)
    private String content;
    @Size(min=3, max=10)
    private String writer;
    private int boardId;

    public PostDto(int id, String title, String content, String writer){//, int boardId
        this.id=id;
        this.title=title;
        this.content=content;
        this.writer=writer;
        //this.boardId=boardId;
    }
    public PostDto(int id){//, int boardId
        this.id=id;
        this.title=title;
        this.content=content;
        this.writer=writer;
        //this.boardId=boardId;
    }
//    @Override
//    public String toString() {
//        return "PostDto{" +
//                "title=" + title + '\'' +
//                ", content=" + content + '\'' +
//                ", writer=" + writer + '\'' +
//                "}";
//    }
}
