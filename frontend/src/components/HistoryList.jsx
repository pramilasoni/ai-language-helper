function HistoryList({ history }) {

  if (history.length === 0) {
    return null;
  }

  return (
    <div className="history-box">

      <h3>Conversation History</h3>

      {history.map((item, index) => (
        <div
          key={index}
          className="history-item"
        >

          <p>
            <strong>You Said:</strong>
          </p>

          <p>{item.transcribed_text}</p>

          <p>
            <strong>AI Response:</strong>
          </p>

          <p>
            {item.response.result_text}
          </p>

        </div>
      ))}
    </div>
  );
}

export default HistoryList;