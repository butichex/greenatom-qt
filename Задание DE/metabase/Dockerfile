FROM gcr.io/google-appengine/openjdk

EXPOSE 8080

ENV PORT 8080
ENV MB_PORT 8080
ENV MB_JETTY_PORT 8080
ENV MB_DB_PORT 5432
ENV METABASE_SQL_INSTANCE postgresql://postgres:Butichex2002!@db.jhgrhvqcbqhbkrmwkans.supabase.co:5432/postgres
ENV JAVA_OPTS "-XX:+IgnoreUnrecognizedVMOptions -Dfile.encoding=UTF-8 --add-opens=java.base/java.net=ALL-UNNAMED --add-modules=java.xml.bind"

ADD https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 ./cloud_sql_proxy
ADD http://downloads.metabase.com/v0.32.9/metabase.jar ./metabase.jar

RUN chmod +x ./cloud_sql_proxy

CMD ./cloud_sql_proxy -instances=$METABASE_SQL_INSTANCE=tcp:$MB_DB_PORT & java -jar ./metabase.jar