resource "aws_glue_catalog_database" "enem_db" {
  name = "dl_enem_delivery_zone"
}

resource "aws_glue_crawler" "enem_anon" {
  database_name = aws_glue_catalog_database.enem_db.name
  name          = "enem_anon_crawler"
  role          = aws_iam_role.glue_role.arn

  s3_target {
    path = "s3://delivery-zone-741358071637/enem_anon/"
  }
}

resource "aws_glue_crawler" "enem_uf_final" {
  database_name = aws_glue_catalog_database.enem_db.name
  name          = "enem_uf_final_crawler"
  role          = aws_iam_role.glue_role.arn

  s3_target {
    path = "s3://delivery-zone-741358071637/enem_uf_final/"
  }
}