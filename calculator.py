

from pyscript import document


def compute_gwa(event):
    """Compute and display the student's GWA and grade summary."""
    first_name = document.getElementById("first_name").value.strip().title()
    last_name = document.getElementById("last_name").value.strip().title()

    # Retrieve and validate grades
    try:
        grades = {
            "Science": float(document.getElementById("science").value),
            "Math": float(document.getElementById("math").value),
            "English": float(document.getElementById("english").value),
            "Filipino": float(document.getElementById("filipino").value),
            "ICT": float(document.getElementById("ict").value),
            "PE": float(document.getElementById("pe").value),
        }
    except ValueError:
        document.getElementById("summary").innerText = (
            "⚠ Please fill in all fields with valid numeric grades."
        )
        document.getElementById("average").innerText = ""
        return

    # Units for each subject (as list of tuples)
    subject_units = [
        ("Science", 3),
        ("Math", 3),
        ("English", 3),
        ("Filipino", 3),
        ("ICT", 2),
        ("PE", 1),
    ]

    # Compute weighted average
    total_units = sum(units for _, units in subject_units)
    total_weight = sum(grades[subj] * units for subj, units in subject_units)
    gwa = total_weight / total_units

    # Display summary
    summary_text = f"Name: {first_name} {last_name}\n\n"
    for subj, grade in grades.items():
        summary_text += f"{subj}: {grade}\n"

    document.getElementById("summary").innerText = summary_text
    document.getElementById("average").innerText = (
        f"Your general weighted average is {gwa:.2f}"
    )
