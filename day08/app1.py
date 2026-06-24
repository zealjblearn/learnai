import chromadb
from pprint import pprint

print(chromadb)

client = chromadb.PersistentClient("./chroma_db")
collection = client.get_or_create_collection("documents_notes_100")
print(collection)

documents = [
    "Sachin Tendulkar is one of the greatest cricketers.",
    "Virat Kohli is a modern cricket legend.",
    "MS Dhoni is known for his calm leadership.",
    "Rohit Sharma has scored multiple double centuries in ODIs.",
    "Jasprit Bumrah is one of the best fast bowlers in the world.",
    "Hardik Pandya is a powerful all-rounder.",
    "Ravindra Jadeja is famous for his fielding skills.",
    "KL Rahul is a versatile Indian batsman.",
    "Shubman Gill is one of India's promising young cricketers.",
    "Yuvraj Singh played a key role in India's 2011 World Cup victory.",

    "Python is a programming language.",
    "Java is widely used for enterprise applications.",
    "C# is commonly used for .NET development.",
    "JavaScript powers interactive web applications.",
    "TypeScript is a superset of JavaScript.",
    "Angular is a frontend framework developed by Google.",
    "React is a popular JavaScript library.",
    "Vue.js is a progressive frontend framework.",
    "ASP.NET Core is used for building web APIs.",
    "Entity Framework Core is an ORM for .NET.",

    "Machine Learning enables systems to learn from data.",
    "Deep Learning uses neural networks with many layers.",
    "Artificial Intelligence is transforming industries.",
    "Natural Language Processing helps computers understand language.",
    "Large Language Models are trained on massive datasets.",
    "Generative AI can create text, images, and code.",
    "Random Forest is an ensemble learning algorithm.",
    "Decision Trees are easy to interpret machine learning models.",
    "Logistic Regression is used for classification problems.",
    "Linear Regression predicts continuous values.",

    "NumPy is used for numerical computing in Python.",
    "Pandas is used for data analysis and manipulation.",
    "Matplotlib is used for data visualization.",
    "Scikit-learn provides machine learning tools.",
    "TensorFlow is a deep learning framework.",
    "PyTorch is widely used in AI research.",
    "Jupyter Notebook is popular among data scientists.",
    "OpenCV is used for computer vision applications.",
    "Keras simplifies deep learning model creation.",
    "Seaborn provides statistical data visualizations.",

    "Azure Functions support serverless computing.",
    "Microsoft Azure offers cloud computing services.",
    "AWS is the world's largest cloud platform.",
    "Google Cloud provides scalable cloud solutions.",
    "Docker is used for containerization.",
    "Kubernetes manages containerized applications.",
    "Git is a version control system.",
    "GitHub hosts software repositories.",
    "Azure DevOps supports CI/CD pipelines.",
    "Terraform enables infrastructure as code.",

    "SQL Server is a relational database system.",
    "MySQL is a popular open-source database.",
    "PostgreSQL is known for advanced features.",
    "MongoDB is a NoSQL database.",
    "Redis is an in-memory data store.",
    "Elasticsearch is used for search and analytics.",
    "Data warehouses store historical business data.",
    "Indexes improve database query performance.",
    "Stored procedures encapsulate database logic.",
    "Normalization reduces data redundancy.",

    "The Taj Mahal is located in India.",
    "The Eiffel Tower is located in Paris.",
    "The Great Wall is one of China's landmarks.",
    "Mount Everest is the world's highest mountain.",
    "The Amazon Rainforest is the largest tropical rainforest.",
    "The Pacific Ocean is the largest ocean.",
    "The Nile is one of the longest rivers.",
    "Tokyo is the capital of Japan.",
    "New Delhi is the capital of India.",
    "Canberra is the capital of Australia.",

    "Lion is known as the king of the jungle.",
    "Tiger is the national animal of India.",
    "Elephants are the largest land mammals.",
    "Dolphins are highly intelligent marine animals.",
    "Penguins cannot fly but are excellent swimmers.",
    "Eagles have excellent eyesight.",
    "Cheetahs are the fastest land animals.",
    "Giraffes are the tallest land animals.",
    "Kangaroos are native to Australia.",
    "Pandas primarily eat bamboo.",

    "The Sun is the center of the solar system.",
    "Earth revolves around the Sun.",
    "Mars is known as the Red Planet.",
    "Jupiter is the largest planet in the solar system.",
    "Saturn is famous for its rings.",
    "The Moon is Earth's natural satellite.",
    "A light-year measures astronomical distance.",
    "Black holes have extremely strong gravity.",
    "The Milky Way is our galaxy.",
    "Astronomy studies celestial objects.",

    "Reading books improves knowledge.",
    "Regular exercise improves health.",
    "Meditation can reduce stress.",
    "Healthy eating supports overall wellness.",
    "Time management increases productivity.",
    "Teamwork improves project outcomes.",
    "Communication is a valuable professional skill.",
    "Continuous learning helps career growth.",
    "Problem solving is a critical skill.",
    "Leadership inspires teams to achieve goals.",

    "Football is the world's most popular sport.",
    "Cricket is widely followed in India.",
    "Tennis is played on different court surfaces.",
    "Basketball was invented by James Naismith.",
    "Olympic Games are held every four years.",
    "Chess is a strategic board game.",
    "Swimming is a full-body workout.",
    "Badminton requires speed and agility.",
    "Formula One is a premier motorsport competition.",
    "Golf is played on a course with multiple holes."
]

ids = [str(i + 1) for i in range(len(documents))]

collection.add(
    documents=documents,
    ids=ids
)
data = collection.get(include=["documents", "embeddings"])

# for i in range(len(data["ids"])):
#     print("\nID:", data["ids"][i])
#     print("Embedding Size:", len(data["embeddings"][i]))
#     print("Embedding:", data["embeddings"][i])

# print(collection.count())

# # result = collection.query(query_texts="Sachin")

# # result = collection.query(query_texts="Sachin", n_results=1)
# # pprint(result)

# result = collection.query(query_texts="Top programming language", n_results=5)
# pprint(result)

result = collection.query(query_texts="Top Football players", n_results=5)
pprint(result)

# # Vector Database