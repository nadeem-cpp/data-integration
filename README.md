# data-processing
<h1><i>Integrating data from differnt sources into a single warehouse AWS Redshift</i></h1>
<br>
<h1 align="center">In Progess</h1>

<h1>Data Integration and Processing System</h1>

<p>This system allows users to seamlessly upload data from different sources in various formats, such as CSV and Excel. The data integration process begins with the system prompting users to identify columns that contain similar values but have different names due to varying sources. Once identified, the system proceeds to process and store the integrated data in Redshift, a powerful data warehousing solution, or allows users to download it for local storage.</p>

<h2>Key Features:</h2>

<ol>
  <li><strong>Data Upload:</strong> Users can upload data from different sources, including CSV and Excel files, ensuring compatibility with a wide range of formats.</li>
  
  <li><strong>Column Matching:</strong> The system intelligently prompts users to match columns with similar values but different names from various sources. This step streamlines the data integration process and ensures accuracy.</li>
  
  <li><strong>Data Processing:</strong> The system performs advanced processing and transformation on the integrated data to derive valuable insights. Users can define specific rules and transformations to be applied during this step.</li>
  
  <li><strong>Storage Options:</strong> Integrated data can be seamlessly stored in Redshift, a high-performance data warehousing solution, which enables efficient querying and analysis. Alternatively, users can choose to download the integrated data for local storage or further processing.</li>
  
  <li><strong>Messaging Bot:</strong> The system includes a messaging interface that facilitates direct communication between clients and technical personnel via WhatsApp. Clients can send messages through the app's user interface, and the responses from technical personnel are displayed in real-time.</li>
  
  <li><strong>Google Authentication:</strong> The app is protected by Google Authentication, ensuring secure user authentication. However, users who do not wish to use authentication can still perform data integration. In this case, their integrated data will be temporarily stored in S3. They can download the data but will not have the ability to perform queries or save the data to Redshift. After the session ends, all their data will be wiped out of S3 and cannot be saved again without authentication.</li>
</ol>

<p>By leveraging this data integration and processing system, users can effortlessly integrate and process data from multiple sources, enabling them to gain valuable insights and make informed decisions. The intuitive user interface and powerful features make it a reliable and efficient solution for managing complex data integration tasks.</p>

<p>For detailed instructions on how to use the system, please refer to the documentation provided in the repository.</p>

