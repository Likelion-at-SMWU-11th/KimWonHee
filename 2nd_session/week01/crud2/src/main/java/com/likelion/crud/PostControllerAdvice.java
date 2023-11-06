package com.likelion.crud;

import com.likelion.crud.exception.BaseException;
import com.likelion.crud.exception.ErrorResponseDto;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestControllerAdvice
public class PostControllerAdvice {
    @ExceptionHandler(BaseException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ErrorResponseDto handleBaseException(BaseException exception){ //다른거 다 주석, 얘는 복붙해오되 @ResponseBody 추가
        return new ErrorResponseDto(exception.getMessage());
    }
}
