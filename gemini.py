import google.generativeai as genai
import os

genai.configure(api_key="")

model = genai.GenerativeModel("gemini-2.5-flash")

prompt = f"""
You are a LinkedIn profile reviewer.

Review the following headline and about section and give:
1. 3 headline improvement suggestions
2. 3 about section improvement suggestions
3. One rewritten headline
4. One rewritten about section

Headline:
Soham Sharma - Gen AI Trainer | AI Product Manager

About:
Results-driven Product Manager and Customer Success Leader with 8+ years in the IT industry, specializing in headless Shopify development and innovative e-commerce experiences. I bring a unique blend of product management, AI/ML, and customer success expertise to deliver performant, scalable, and personalized digital storefronts.My core focus is on developing and managing headless e-commerce solutions using technologies like Gatsby, Astro.js, Vue.js, Next.js, and React.js—seamlessly integrated with the Shopify platform. I have a proven track record of managing product lifecycles from concept to launch, driving innovation through Agile methodologies, and prioritizing features that improve user engagement and conversion.I’ve led the implementation of AI/ML features using TensorFlow, Scikit-learn, and PyCaret to enhance product discovery, enable personalized shopping experiences, and support dynamic pricing strategies. Experienced in using Google Cloud AutoML, AWS SageMaker, and Google Vertex AI to scale intelligent product features.My work in product and customer success has reduced churn by 20% and increased retention by 25%, achieved through data-driven user research, journey mapping, and continuous feedback loops. I’ve successfully translated merchant and end-user insights into actionable roadmaps using tools like Aha!, Miro, and ProdPad.Skilled in backlog management, stakeholder alignment, and cross-functional collaboration, I ensure that headless Shopify solutions meet high standards of performance, UX, and compliance (SOC 2, ISO, GDPR). I also leverage analytics tools like Looker, Tableau, and Google Optimize to drive iterative improvements and validate hypotheses through A/B testing.Passionate about modern commerce, I thrive on bridging technical innovation and business value—crafting future-ready e-commerce platforms that scale with customer needs.Results-driven Product Manager and Customer Success Leader with 8+ years in the IT industry, specializing in headless Shopify development and innovative e-commerce experiences. I bring a unique blend of product management, AI/ML, and customer success expertise to deliver performant, scalable, and personalized digital storefronts.

My core focus is on developing and managing headless e-commerce solutions using technologies like Gatsby, Astro.js, Vue.js, Next.js, and React.js—seamlessly integrated with the Shopify platform. I have a proven track record of managing product lifecycles from concept to launch, driving innovation through Agile methodologies, and prioritizing features that improve user engagement and conversion.

I’ve led the implementation of AI/ML features using TensorFlow, Scikit-learn, and PyCaret to enhance product discovery, enable personalized shopping experiences, and support dynamic pricing strategies. Experienced in using Google Cloud AutoML, AWS SageMaker, and Google Vertex AI to scale intelligent product features.

My work in product and customer success has reduced churn by 20% and increased retention by 25%, achieved through data-driven user research, journey mapping, and continuous feedback loops. I’ve successfully translated merchant and end-user insights into actionable roadmaps using tools like Aha!, Miro, and ProdPad.
"""

response = model.generate_content(prompt)

print("\n------ GEMINI PROFILE REVIEW ------\n")
print(response.text)
