package com.likelion.crud.post;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;
import java.util.List;

public class ValidTestDto {
    @NotNull
    private String notNullString;
    @NotEmpty
    private String notEmptyString;
    @NotBlank
    private String notBlankString;

    @NotEmpty
    private List<String> notEmptyStringList;

    public ValidTestDto(){

    }
    @Override
    public String toString() {
        return "ValidTestDto{" +
                "notNullString='" + notNullString + '\'' +
                ", notEmptyString='" + notEmptyString + '\'' +
                ", notBlankString='" + notBlankString + '\'' +
                ", notEmptyStringList=" + notEmptyStringList +
                '}';
    }

    public ValidTestDto(String notNullString, String notEmptyString, String notBlankString, List<String> notEmptyStringList){
        this.notBlankString=notBlankString;
        this.notEmptyString=notEmptyString;
        this.notNullString=notNullString;
        this.notEmptyStringList=notEmptyStringList;
    }

    public String getNotNullString() {
        return notNullString;
    }

    public void setNotNullString(String notNullString) {
        this.notNullString = notNullString;
    }

    public String getNotEmptyString() {
        return notEmptyString;
    }

    public void setNotEmptyString(String notEmptyString) {
        this.notEmptyString = notEmptyString;
    }

    public String getNotBlankString() {
        return notBlankString;
    }

    public void setNotBlankString(String notBlankString) {
        this.notBlankString = notBlankString;
    }

    public List<String> getNotEmptyStringList() {
        return notEmptyStringList;
    }

    public void setNotEmptyStringList(List<String> notEmptyStringList) {
        this.notEmptyStringList = notEmptyStringList;
    }
}

