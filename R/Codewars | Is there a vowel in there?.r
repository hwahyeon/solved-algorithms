 is_vow <- function(a){
   if(sum(a %in% c(97, 101, 105, 111, 117)) == 0) {a
  }else{
      a<-gsub(97,"a", a)
      a<-gsub(101,"e", a)
      a<-gsub(105,"i", a)
      a<-gsub(111,"o", a)
      a<-gsub(117,"u", a)
  }
 }
