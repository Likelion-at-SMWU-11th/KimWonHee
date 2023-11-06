package com.likelion.crud;

import com.likelion.crud.exception.BaseException;
import com.likelion.crud.exception.ErrorResponseDto;
import com.likelion.crud.exception.PostNotExistException;
import com.likelion.crud.exception.PostNotInBoardException;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

@RestController
@RequestMapping("except")
public class ExceptionTestController {
    @GetMapping("/{id}")
    public void throwException(@PathVariable int id){
        switch (id){
            case 1: // http://localhost:8080/except/1
                throw new PostNotExistException();
            case 2: // http://localhost:8080/except/2
                throw new PostNotInBoardException();
            default:
                throw new ResponseStatusException(HttpStatus.NOT_FOUND);
        }
    }
    //컨트롤러나 레스트컨트롤러 안에서만 사용가능함..??
//    @ExceptionHandler(BaseException.class)
//    @ResponseStatus(HttpStatus.BAD_REQUEST)
//    public ErrorResponseDto handleBaseException(BaseException exception){
//        return new ErrorResponseDto(exception.getMessage());
//    }
}
