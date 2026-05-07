function ModeSelector({
  mode,
  setMode,
  targetLanguage,
  setTargetLanguage,
}) {

  return (
    <>
      <div className="form-section">

        <label>Choose Mode</label>

        <select
          value={mode}
          onChange={(e) => setMode(e.target.value)}
        >
            <option value="auto">
          Auto detect intent
          </option>
          <option value="correct">
            Correct my sentence
          </option>

          <option value="translate">
            Translate my sentence
          </option>
            
        </select>
      </div>

      {mode === "translate" && (
        <div className="form-section">

          <label>Target Language</label>

          <input
            value={targetLanguage}
            onChange={(e) =>
              setTargetLanguage(e.target.value)
            }
            placeholder="Example: Danish"
          />

        </div>
      )}
    </>
  );
}

export default ModeSelector;