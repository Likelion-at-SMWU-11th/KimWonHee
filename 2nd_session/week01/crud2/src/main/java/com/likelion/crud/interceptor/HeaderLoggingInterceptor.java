package com.likelion.crud.interceptor;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import org.springframework.web.method.HandlerMethod;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Collection;
import java.util.Enumeration;
@Component
public class HeaderLoggingInterceptor implements HandlerInterceptor {
    private static final Logger logger= LoggerFactory.getLogger(HeaderLoggingInterceptor.class);
   // @Override
//    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
//        HandlerMethod handlerMethod=(HandlerMethod) handler;
//        logger.info("start processing of {}", handlerMethod.getMethod().getName());
//        Enumeration<String> headerNames=request.getHeaderNames();
//        while (headerNames.hasMoreElements()){
//            String headerName=headerNames.nextElement();
//            logger.info("{}={}", headerName, request.getHeader(headerName));
//        }
//        return true;
//    }
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        if (handler instanceof HandlerMethod) {
            HandlerMethod handlerMethod = (HandlerMethod) handler;
            logger.info("start processing of {}", handlerMethod.getMethod().getName());
            Enumeration<String> headerNames = request.getHeaderNames();
            while (headerNames.hasMoreElements()) {
                String headerName = headerNames.nextElement();
                logger.info("{}={}", headerName, request.getHeader(headerName));
            }
        }

        return true;
    }


    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        Collection<String> headerNames=response.getHeaderNames();
        for (String headerName: headerNames){
            logger.info("{}={}", headerName, response.getHeader(headerName));
        }
    }

    //header 알아보기위한과정임이건다..
    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        HandlerMethod handlerMethod=(HandlerMethod) handler;
        logger.info("end processing of {}", handlerMethod.getMethod().getName());
        if (ex!= null) logger.error("Exception occurred while processing, ", ex);
    }
}
