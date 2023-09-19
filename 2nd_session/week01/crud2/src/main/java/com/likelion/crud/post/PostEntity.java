package com.likelion.crud.post;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Table(name="post")
@Getter
@Setter
@NoArgsConstructor

public class PostEntity extends BaseEntity{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private String content;
    private String writer;
    @JoinColumn(name="board_id")
    @ManyToOne(
            targetEntity = BoardEntity.class,
            fetch=FetchType.LAZY
    )
    private BoardEntity boardEntity;
}
