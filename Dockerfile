FROM python:3.11

COPY app.py app.py

RUN pip3 install streamlit

# Instalar Java 11
RUN wget https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz && \
    tar -xvzf openjdk-11.0.2_linux-x64_bin.tar.gz && \
    mv jdk-11.0.2 /opt/java-11 && \
    echo "export JAVA_HOME=/opt/java-11" >> /etc/profile.d/java.sh && \
    echo "export PATH=\$JAVA_HOME/bin:\$PATH" >> /etc/profile.d/java.sh

# Instalar Maven
RUN wget https://archive.apache.org/dist/maven/maven-3/3.5.3/binaries/apache-maven-3.5.3-bin.tar.gz && \
    tar -xvzf apache-maven-3.5.3-bin.tar.gz && \
    mv apache-maven-3.5.3 /opt/maven && \
    echo "export M2_HOME=/opt/maven" >> /etc/profile.d/maven.sh && \
    echo "export MAVEN_HOME=/opt/maven" >> /etc/profile.d/maven.sh && \
    echo "export PATH=\$M2_HOME/bin:\$PATH" >> /etc/profile.d/maven.sh

# Establecer variables de entorno en el contenedor
ENV JAVA_HOME /opt/java-11
ENV M2_HOME /opt/maven
ENV MAVEN_HOME /opt/maven
ENV PATH $JAVA_HOME/bin:$M2_HOME/bin:$PATH

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=80", "--server.address=0.0.0.0"]
