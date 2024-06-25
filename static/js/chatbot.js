const askButton = document.getElementById('ask-button');
const userQueryInput = document.getElementById('user-query');
const answerContainer = document.getElementById('answer-container');

askButton.addEventListener('click', async () => {
  const userQuery = userQueryInput.value.trim();
  if (!userQuery) {
    alert('Please enter a question about Indian Law.');
    return;
  }

  // Replace with your actual API endpoint URL (assuming it's running on the same server)
  const apiUrl = '/get_answer';

  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_query: userQuery }),
    });

    const data = await response.json();

    if (data.error) {
      throw new Error(data.error);
    }

    answerContainer.textContent = data.answer;
  } catch (error) {
    console.error(error);
    answerContainer.textContent = 'An error occurred. Please try again later.';
  } finally {
    userQueryInput.value = '';  // Clear user input after processing
  }
});
