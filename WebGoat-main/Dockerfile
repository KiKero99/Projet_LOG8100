 # Stage 1: Build the WebGoat application

 FROM maven:3.8-openjdk-21-slim AS builder

 WORKDIR /build
 COPY . .
 
 # Use Maven directly to build the project
 RUN mvn clean install 
 
 # Stage 2: Create the WebGoat runtime image
 FROM docker.io/eclipse-temurin:21-jdk-jammy
 
 LABEL name="WebGoat: A deliberately insecure Web Application"
 LABEL maintainer="WebGoat team"
 
 RUN \
   useradd -ms /bin/bash webgoat && \
   chgrp -R 0 /home/webgoat && \
   chmod -R g=u /home/webgoat
 
 USER webgoat
 
 # Copy the built JAR from the builder stage
 COPY --from=builder /build/target/webgoat-*.jar /home/webgoat/webgoat.jar
 
 EXPOSE 8080
 EXPOSE 9090
 
 ENV TZ=Europe/Amsterdam
 
 WORKDIR /home/webgoat
 ENTRYPOINT [ "java", \
    "-Duser.home=/home/webgoat", \
    "-Dfile.encoding=UTF-8", \
    "--add-opens", "java.base/java.lang=ALL-UNNAMED", \
    "--add-opens", "java.base/java.util=ALL-UNNAMED", \
    "--add-opens", "java.base/java.lang.reflect=ALL-UNNAMED", \
    "--add-opens", "java.base/java.text=ALL-UNNAMED", \
    "--add-opens", "java.desktop/java.beans=ALL-UNNAMED", \
    "--add-opens", "java.desktop/java.awt.font=ALL-UNNAMED", \
    "--add-opens", "java.base/sun.nio.ch=ALL-UNNAMED", \
    "--add-opens", "java.base/java.io=ALL-UNNAMED", \
    "--add-opens", "java.base/java.util=ALL-UNNAMED", \
    "--add-opens", "java.base/sun.nio.ch=ALL-UNNAMED", \
    "--add-opens", "java.base/java.io=ALL-UNNAMED", \
    "-Drunning.in.docker=true", \
    "-jar", "webgoat.jar", "--server.address", "0.0.0.0" ]
 
 HEALTHCHECK --interval=5s --timeout=3s \
   CMD curl --fail http://localhost:8080/WebGoat/actuator/health || exit 1