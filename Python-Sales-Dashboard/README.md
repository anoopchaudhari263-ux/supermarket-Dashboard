# Python-Sales-Dashboard

<h4>Question:</h4> Using Python and the sales datasheet, create a dashboard that shows total sales, average rating, and sales per transaction. Create graphs to display visual insights into the data and use multiple filters that users can choose from.

This was my first attempt at creating a dashboard using Python. This is the link to the tutorial I followed to create the dashboard and answer the above question: https://www.youtube.com/watch?v=Sb0A9i6d320&list=PLbyxRwpy0b2Yc-nQ1xcjCVt63b0mT8bJb&index=49&ab_channel=CodingIsFun

The data used was already clean and usable. First, we need to import the libraries used to create the dashboard (Pandas, Plotly Express, and Streamlit), then we can move on to importing the Excel sheet into Python.

<img src="https://github.com/LeFrenchy5/Python-Stock-Market-Dashboard/assets/123564919/4dfc144c-4b65-413e-b5dd-c3d4bfc416d9" width="90%"></img>
<h6>Excel Sheet</h6>

We added a title and a sidebar that will house the filters (city, gender, and customer type).

<img src="https://github.com/LeFrenchy5/Python-Stock-Market-Dashboard/assets/123564919/0fd42c71-d18d-455e-8274-6d88e625689a" width="90%"></img> 
<h6>Python Code</h6>

We created the main page, which will have the title of the dashboard as well as the KPI's asked for in the question (total sales, average rating, and average sales per transaction).

<img src="https://github.com/LeFrenchy5/Python-Stock-Market-Dashboard/assets/123564919/3a55d720-567b-49d9-9302-f177c4a1e9f6" width="90%"></img> 
<h6>Python Code</h6>

The final part was to create two graphs to display some visual insights (hourly sales and product sales).
We finished the project by hiding the Streamlit footers and headers.

<img src="https://github.com/LeFrenchy5/Python-Stock-Market-Dashboard/assets/123564919/81a841f3-a07f-4b46-95b1-843d7e784f77" width="90%"></img> 
<h6>Python Code</h6>

<img src="https://github.com/LeFrenchy5/Python-Stock-Market-Dashboard/assets/123564919/02170f5c-3af5-4b98-8f25-358cb31a25a8" width="90%"></img>
<h6>Dashboard</h6>

<h4>Conclusion:</h4> To conclude, this dashboard is very simple and displays the bare minimum. The color scheme and font work well together, and the dashboard is not overcrowded, but it does lack any true deep insights into the data. The coding has an issue when no filters are selected, the KPIs display NaN rather than zero, and the Pandas library was underutilized. These are a few areas I would like to improve on in order to make this dashboard better and more insightful.

However, I am happy with having learned Streamlit and learning that it is quite easy to use and very user-friendly. So I will be creating many more dashboards in Python when more complex graphs and calculations are needed.
