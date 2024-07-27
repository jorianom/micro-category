FROM python
WORKDIR /app
COPY . .
COPY requirements.txt .
ENV MONGO_URI=mongodb+srv://jorianom:HnvfGLi4lqiK3i4t@cluster0.galso05.mongodb.net/CategoriesDB?retryWrites=true&w=majority&appName=Cluster0
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "src/app.py"]