# Employment Assessment App

## Project Overview
This app leverages AI to assess candidates’ fit based on customizable HR-defined criteria, including flexible cognitive assessments that allow candidates to choose the type best suited to their cognitive strengths.

## Key Features
- **Modular Assessment Criteria**: Allows HR to define, customize, and weigh various criteria based on role requirements.
- **Flexible Cognitive Assessment Options**: Supports multiple assessment types (e.g., Raven’s Progressive Matrices for visual processors).
- **Role-Specific Configurations**: Enables HR to tailor assessment requirements and weights by job role.
- **Candidate-Friendly Interface**: Provides guidance on selecting assessments best aligned with each candidate’s cognitive strengths.
- **Core Values Module**: Allows HR to adjust weightings for core values like collaboration, innovation, and adaptability.

## Technologies
- **Backend**: Python, Django/Flask
- **Frontend**: React or Vue.js
- **Database**: PostgreSQL or MongoDB
- **Machine Learning**: TensorFlow/PyTorch

## High-Level Roadmap
### Phase 1: Criteria Definition & Data Preparation
- Define modular criteria structure and database schema.
- Implement HR interface for defining and managing criteria, including adding, removing, and adjusting assessment criteria, as well as defining weights for each criterion.

### Phase 2: Model Development
- Train predictive models for scoring assessments.
- Integrate AI modules with assessment results.

### Phase 3: User Interface Design
- Develop candidate and HR interfaces for selecting assessments and customizing criteria.

### Phase 4: Testing & Evaluation
- Conduct extensive testing to ensure accuracy and bias-free assessments.

### Phase 5: Deployment & Maintenance
- Deploy the app and set up monitoring and continuous improvement cycles.

## Role-Specific Customization Module

### Overview
The role-specific customization module allows HR to configure specific criteria for each role with relevant weights, linked assessments, and customization options. This module provides a flexible and comprehensive way to tailor assessment requirements based on the unique needs of each job role.

### Features
- **Role Management**: Create, update, and delete roles with specific criteria and linked assessments.
- **Criteria Management**: Define, customize, and weigh criteria for each role.
- **Linked Assessments**: Link specific assessments to roles and manage their details.

### Instructions for HR
1. **Access the Role Customization Module**: Navigate to the HR dashboard and click on the "Role Customization" link.
2. **Create a New Role**:
   - Click on "Add Role".
   - Enter the role name and description.
   - Save the role.
3. **Define Criteria for a Role**:
   - Select a role from the list.
   - Click on "Add Criteria".
   - Enter the criteria name and weight.
   - Save the criteria.
4. **Link Assessments to a Role**:
   - Select a role from the list.
   - Click on "Add Linked Assessment".
   - Enter the assessment name and description.
   - Save the linked assessment.
5. **Update or Delete Roles, Criteria, and Linked Assessments**:
   - Use the edit and delete options available in the role, criteria, and linked assessment lists.

By following these instructions, HR can effectively manage role-specific criteria and assessments, ensuring that each role has tailored assessment requirements that align with the organization's needs.

## Deployment to Github Pages

### Prerequisites
- Ensure you have a Github repository for your project.
- Ensure you have Github Pages enabled for your repository.

### Steps
1. **Add `homepage` to `package.json`**:
   - Open `react_app/package.json`.
   - Add the following line: `"homepage": "https://<your-github-username>.github.io/<your-repo-name>"`.

2. **Update Github Actions Workflow**:
   - Open `.github/workflows/main.yml`.
   - Add the following steps to the `deploy` job:
     ```yaml
     - name: Configure Git user
       run: |
         git config --global user.name 'github-actions[bot]'
         git config --global user.email 'github-actions[bot]@users.noreply.github.com'

     - name: Build React app
       run: |
         cd react_app
         npm run build

     - name: Deploy to Github Pages
       run: |
         cd react_app
         git init
         git add build
         git commit -m 'Deploy to Github Pages'
         git push --force --quiet "https://${{ secrets.GITHUB_TOKEN }}@github.com/<your-github-username>/<your-repo-name>.git" master:gh-pages
     ```

3. **Commit and Push Changes**:
   - Commit and push the changes to your repository.
   - Github Actions will automatically build and deploy your React app to Github Pages.

4. **Access Your Deployed App**:
   - Open your browser and navigate to `https://<your-github-username>.github.io/<your-repo-name>` to see your deployed React app.
