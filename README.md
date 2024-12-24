# Document Search Engine Frontend

### Installation
   
1. **Navigate to the Project Directory**:
   Move into the cloned project directory:
   ```bash
   cd doc-search-engine-frontend
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:
   
   _Notes:_ Before creating a new `venv`, make sure you've deletec all the existing hidden `venv` in your directory.

   It's recommended to create a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
   This will install all the necessary packages, including Streamlit and any other libraries used by the applications.

4. **Run the Streamlit Application**:
   You can run any of the Streamlit applications using the following command:
   ```bash
   streamlit run Main.py
   ```

5. **Access the Application**:
   Once the application is running, open your web browser and go to `http://localhost:8502` to interact with the app.

6. **Deploying the Application (Optional)**:
   If you want to deploy your Streamlit application to a server or a cloud platform, consider using Streamlit Cloud, Heroku, or any other hosting service. Ensure you have configured your environment variables and dependencies accordingly for production.

By following these steps, you should be able to set up and run the Streamlit applications smoothly on your local machine.