"""
    Util file! ^_^

    p_uncorrected,p_fdr_bh,p_bonferroni,p_sidak,p_holm_sidak,
    p_holm,p_simes_hochberg,p_hommel,p_fdr_by,p_fdr_tsbh,p_fdr_gbs,p_fdr_tsbky
"""

# hashtable that contians the conversion from their name in gui to the name in the csv file
defaultCorrection = "Select a correction method"
correctionNameConversions = {
    defaultCorrection: None,
    "Uncorrected":     "p_uncorrected",
    "Fdr-bh":          "p_fdr_bh",
    "Holm":            "p_holm",
    "Sidak":           "p_sidak",
    "Holm-Sidak":      "p_holm_sidak",
    "Bonferroni":      "p_bonferroni",
    "Simes-Hochberg":  "p_simes_hochberg",
    "Hommel":          "p_hommel",
    "Fdr-by":          "p_fdr_by",
    "Fdr-tsbh":        "p_fdr_tsbh",
    "Fdr-gbs":         "p_fdr_gbs",
    "Fdr-tsbky":       "p_fdr_tsbky",
}
# the spacing is a bit extra i know but it's still nice :)
